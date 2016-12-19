import os,gzip,tarfile
import zipfile,rarfile
#解压文件,其中gzip为gz(只压缩一个文件)

def un_gz(file_name):	#解压gzip压缩文件
	f_name = file_name.replace(".gz", "")	#获取文件的名称，去掉  
	g_file = gzip.GzipFile(file_name)	#创建gzip对象  
	open(f_name, "w+").write(g_file.read())	#gzip对象用read()打开后，写入open()建立的文件中。  
	g_file.close()	#关闭gzip对象  
    
def un_tar(file_name,uz_folder):	#解压tar文件
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

def un_rar(file_name,uz_folder=None):	#解压rar文件，第二个参数为解压目录
	rar	= rarfile.RarFile(file_name)
	if(uz_folder is None):
		if(os.path.isdir(file_name+"_files")):		#解压到当前文件夹
			pass
		else:
			os.mkdir(file_name+"_files")		
		os.chdir(file_name+"files")
	else:
		os.chdir(uz_folder)
	rar.extractall()
	rar.close()