# __*__ coding:UTF-8 __*__

import os,sys,hashlib
import random

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
	for file_dir in os.listdir(path_name):
		midPath2=path_name+'\\'+file_dir
		if(os.path.isfile(midPath2)):
			list_file_dir.append(midPath2)
			#print midPath2
#print list_file_dir
dic_file_md5=GetFileMD5(list_file_dir)	#�����ļ���md5��
#print dic_file_md5
#ѭ��ÿ���ļ��ж�ÿ���ļ��������ļ��Ƿ������ͬ��md5
list_homework=CheckFileIsRepeat(dic_file_md5)
#print dic_file_repeat
for obj_homework in list_homework:
	print (obj_homework.student_num+',�ɼ���' +str(obj_homework.score))

