import os,gzip,tarfile
import zipfile,rarfile
#��ѹ�ļ�,����gzipΪgz(ֻѹ��һ���ļ�)

def un_gz(file_name):	#��ѹgzipѹ���ļ�
	f_name = file_name.replace(".gz", "")	#��ȡ�ļ������ƣ�ȥ��  
	g_file = gzip.GzipFile(file_name)	#����gzip����  
	open(f_name, "w+").write(g_file.read())	#gzip������read()�򿪺�д��open()�������ļ��С�  
	g_file.close()	#�ر�gzip����  
    
def un_tar(file_name,uz_folder):	#��ѹtar�ļ�
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

def un_rar(file_name,uz_folder=None):	#��ѹrar�ļ����ڶ�������Ϊ��ѹĿ¼
	rar	= rarfile.RarFile(file_name)
	if(uz_folder is None):
		if(os.path.isdir(file_name+"_files")):		#��ѹ����ǰ�ļ���
			pass
		else:
			os.mkdir(file_name+"_files")		
		os.chdir(file_name+"files")
	else:
		os.chdir(uz_folder)
	rar.extractall()
	rar.close()