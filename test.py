# __*__ coding:UTF-8 __*__

import os,sys,hashlib
import random,gzip,tarfile
import zipfile,rarfile

#��ҵ��					
class homework:
	score=0	#����
	student_num=''	#ѧ��
	hasfile=1 #�Ƿ����ļ�
	file_md5=''	#�ļ�md5
	is_repeat=0	#�Ƿ���������ͬ�ļ�
	def correctScore(self):	#���ַ���
		if(self.hasfile==0):	#����ļ�Ϊ��������Ϊ0
			score=0
		else:
			if(self.is_repeat==1):	#���ظ��ļ�������Ϊ6-8��
				self.score=round(random.uniform(9.0,9.7),1)
			else:	#����������Ϊ9-10��
				self.score=round(random.uniform(9.8,10.0),1)

#��ȡ����ҵ��md5ֵ����
def GetFileMD5(list_file_dir):
	dic_file_md5=dict()	#�����ļ���md5��
	for file_dir in list_file_dir:
		if(os.path.isfile(file_dir)):
			obj_file=open(file_dir,'rb')
			dic_file_md5[file_dir]=hashlib.new('md5',obj_file.read()).hexdigest() 
	return dic_file_md5

#�����б�����ͬMD5ֵ������
def CheckFileIsRepeat(dic_file_md5):
	list_homework=[]
	for i in range(0,len(dic_file_md5.keys())-1):
		dic_file_key=list(dic_file_md5.keys())[i]
		c=homework()
		c.student_num=dic_file_key.split('\\')[-2]
		c.file_md5=dic_file_md5[dic_file_key]
		#print '��ʼ�ж�'+dic_file_key
		for j in range(i+1,len(dic_file_md5.keys())-1):
			dic_file_key2=list(dic_file_md5.keys())[j]
			if(dic_file_key==dic_file_key2):
				continue;
			else:
				if(dic_file_md5[dic_file_key]==dic_file_md5[dic_file_key2]):
					c.is_repeat=1
					#print dic_file_key.split('\\')[-2]+'-'+dic_file_key.split('\\')[-1]+"��"+dic_file_md5[dic_file_key]+';'+dic_file_key2.split('\\')[-2]+'-'+dic_file_key2.split('\\')[-1]+'��'+dic_file_md5[dic_file_key]
					#dic_file_repeat[dic_file_key]=dic_file_key2	
		c.correctScore()
		list_homework.append(c)
	return list_homework
	
def un_gz(file_name):	#��ѹgzipѹ���ļ�
	f_name = file_name.replace(".gz", "")	#��ȡ�ļ������ƣ�ȥ��  
	g_file = gzip.GzipFile(file_name)	#����gzip����  
	open(f_name, "w+").write(g_file.read())	#gzip������read()�򿪺�д��open()�������ļ��С�  
	g_file.close()	#�ر�gzip����  
    
def un_tar(file_name):	#��ѹtar�ļ�
	tar = tarfile.open(file_name,uz_folder)
	names=tar.getnames()
	#if(os.path.isdir(file_name+"_files")):		#��ѹ����ǰ�ļ���
	#	pass
	#else:
	#	os.mkdir(file_name+"_files")
	for name in names:	#���������ļ�����ѹ���ض��ļ���
		tar.extract(name,uz_folder)
	tar.close()

def un_zip(file_name,uz_folder):	#��ѹzip�ļ����ڶ�������Ϊ��ѹĿ¼
	zip_file=zipfile.ZipFile(file_name)
	#if(os.path.isdir(file_name+"_files")):		#��ѹ����ǰ�ļ���
	#	pass
	#else:
	#	os.mkdir(file_name+"_files")
	names=zip_file.namelist()
	for name in names:	#���������ļ�����ѹ���ض��ļ���
		zip_file.extract(name,uz_folder)
	zip_file.close()

def un_rar(file_name,uz_folder):	#��ѹrar�ļ����ڶ�������Ϊ��ѹĿ¼
	rar	= rarfile.RarFile(file_name)
	print(rar.getinfo())
	#os.chdir()
	rar.extractall(uz_folder)
	rar.close()

def CheckIsCompress(file_name):	#����Ƿ���ļ���ѹ���ļ�
	rar_files=[".gzip",".tar",".zip",".rar"]
	isCompress=""
	for rar_file in rar_files:
		print("�ж�ѹ���ļ�"+file_name+"���ͣ�"+rar_file)
		print(file_name.find(rar_file))
		if(file_name.find(rar_file)>=0):
			isCompress=rar_file
			break
	return isCompress

def GetAllFileDir(path_name):#��ȡ��ǰ�ļ������е��ļ�ȫ·��
	for file_dir in os.listdir(path_name):
		midPath2=path_name+'\\'+file_dir
		if(os.path.isfile(midPath2)):
			compressType=CheckIsCompress(midPath2)
			if(compressType==""):
				list_file_dir.append(midPath2)
			else:	#���ļ�Ϊѹ���ļ�
				print("��ѹ"+midPath2+"��ʼ...,��ѹ·����"+path_name)
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
	if (os.path.isdir(midpath)):	#�ж��Ƿ����ļ��У�����ǣ������ļ����б�
		list_dir.append(midpath)
#print list_dir		#�����ǰĿ¼�������ļ���
list_file_dir=[]	#�������е��ļ�·��
for path_name in list_dir:	#���������ļ���
	#print path_name
	print("��ǰ������ѧ��Ϊ��"+path_name)
	list_file_dir.append(GetAllFileDir(path_name))
#print list_file_dir
dic_file_md5=GetFileMD5(list_file_dir)	#�����ļ���md5��
#print dic_file_md5
#ѭ��ÿ���ļ��ж�ÿ���ļ��������ļ��Ƿ������ͬ��md5
list_homework=CheckFileIsRepeat(dic_file_md5)
#print dic_file_repeat
for obj_homework in list_homework:
	print (obj_homework.student_num+',�ɼ���' +str(obj_homework.score))
