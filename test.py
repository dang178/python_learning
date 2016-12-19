# __*__ coding:UTF-8 __*__

import os,sys,hashlib
import random,gzip,tarfile
import zipfile,rarfile

#作业类					
class homework:
	score=0	#分数
	student_num=''	#学号
	hasfile=1 #是否有文件
	file_md5=''	#文件md5
	is_repeat=0	#是否有其他相同文件
	def correctScore(self):	#评分方法
		if(self.hasfile==0):	#如果文件为空则评分为0
			score=0
		else:
			if(self.is_repeat==1):	#有重复文件则评分为6-8分
				self.score=round(random.uniform(9.0,9.7),1)
			else:	#正常则评分为9-10分
				self.score=round(random.uniform(9.8,10.0),1)

#获取有作业的md5值方法
def GetFileMD5(list_file_dir):
	dic_file_md5=dict()	#所有文件的md5码
	for file_dir in list_file_dir:
		if(os.path.isfile(file_dir)):
			obj_file=open(file_dir,'rb')
			dic_file_md5[file_dir]=hashlib.new('md5',obj_file.read()).hexdigest() 
	return dic_file_md5

#查找列表中相同MD5值的数据
def CheckFileIsRepeat(dic_file_md5):
	list_homework=[]
	for i in range(0,len(dic_file_md5.keys())-1):
		dic_file_key=list(dic_file_md5.keys())[i]
		c=homework()
		c.student_num=dic_file_key.split('\\')[-2]
		c.file_md5=dic_file_md5[dic_file_key]
		#print '开始判断'+dic_file_key
		for j in range(i+1,len(dic_file_md5.keys())-1):
			dic_file_key2=list(dic_file_md5.keys())[j]
			if(dic_file_key==dic_file_key2):
				continue;
			else:
				if(dic_file_md5[dic_file_key]==dic_file_md5[dic_file_key2]):
					c.is_repeat=1
					#print dic_file_key.split('\\')[-2]+'-'+dic_file_key.split('\\')[-1]+"："+dic_file_md5[dic_file_key]+';'+dic_file_key2.split('\\')[-2]+'-'+dic_file_key2.split('\\')[-1]+'：'+dic_file_md5[dic_file_key]
					#dic_file_repeat[dic_file_key]=dic_file_key2	
		c.correctScore()
		list_homework.append(c)
	return list_homework
	
def un_gz(file_name):	#解压gzip压缩文件
	f_name = file_name.replace(".gz", "")	#获取文件的名称，去掉  
	g_file = gzip.GzipFile(file_name)	#创建gzip对象  
	open(f_name, "w+").write(g_file.read())	#gzip对象用read()打开后，写入open()建立的文件中。  
	g_file.close()	#关闭gzip对象  
    
def un_tar(file_name):	#解压tar文件
	tar = tarfile.open(file_name,uz_folder)
	names=tar.getnames()
	#if(os.path.isdir(file_name+"_files")):		#解压到当前文件夹
	#	pass
	#else:
	#	os.mkdir(file_name+"_files")
	for name in names:	#遍历所有文件，解压到特定文件夹
		tar.extract(name,uz_folder)
	tar.close()

def un_zip(file_name,uz_folder):	#解压zip文件，第二个参数为解压目录
	zip_file=zipfile.ZipFile(file_name)
	#if(os.path.isdir(file_name+"_files")):		#解压到当前文件夹
	#	pass
	#else:
	#	os.mkdir(file_name+"_files")
	names=zip_file.namelist()
	for name in names:	#遍历所有文件，解压到特定文件夹
		zip_file.extract(name,uz_folder)
	zip_file.close()

def un_rar(file_name,uz_folder):	#解压rar文件，第二个参数为解压目录
	rar	= rarfile.RarFile(file_name)
	print(rar.getinfo())
	#os.chdir()
	rar.extractall(uz_folder)
	rar.close()

def CheckIsCompress(file_name):	#检查是否该文件是压缩文件
	rar_files=[".gzip",".tar",".zip",".rar"]
	isCompress=""
	for rar_file in rar_files:
		print("判断压缩文件"+file_name+"类型："+rar_file)
		print(file_name.find(rar_file))
		if(file_name.find(rar_file)>=0):
			isCompress=rar_file
			break
	return isCompress

def GetAllFileDir(path_name):#获取当前文件夹所有的文件全路径
	for file_dir in os.listdir(path_name):
		midPath2=path_name+'\\'+file_dir
		if(os.path.isfile(midPath2)):
			compressType=CheckIsCompress(midPath2)
			if(compressType==""):
				list_file_dir.append(midPath2)
			else:	#若文件为压缩文件
				print("解压"+midPath2+"开始...,解压路径："+path_name)
				if(compressType==".rar"):
					un_rar(midPath2,path_name)
				elif(compressType==".zip"):
					un_zip(midPath2,path_name)
				elif(compressType==".tar"):
					un_tar(midPath2,path_name)
				elif(compressType==".gzip"):
					un_gz(midPath2)
				os.remove(midPath2)
				GetAllFileDir(path_name)
			#print midPath2
	return list_file_dir

base_dir='D:\homework'
list_dir=[]
for path_name in os.listdir(base_dir):
	midpath=base_dir+'\\'+path_name
	#print midpath
	#print os.path.isfile(midpath)
	if (os.path.isdir(midpath)):	#判断是否是文件夹，如果是，加入文件夹列表
		list_dir.append(midpath)
#print list_dir		#输出当前目录下所有文件夹
list_file_dir=[]	#保存所有的文件路径
for path_name in list_dir:	#遍历所有文件夹
	#print path_name
	print("当前遍历的学生为："+path_name)
	list_file_dir.append(GetAllFileDir(path_name))
#print list_file_dir
dic_file_md5=GetFileMD5(list_file_dir)	#所有文件的md5码
#print dic_file_md5
#循环每个文件判断每个文件与其他文件是否具有相同的md5
list_homework=CheckFileIsRepeat(dic_file_md5)
#print dic_file_repeat
for obj_homework in list_homework:
	print (obj_homework.student_num+',成绩：' +str(obj_homework.score))
