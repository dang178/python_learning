# --*-- coding:UTF-8 --*--
import sys
import math

##求出a~maxnum之间第一个素数
def getprime(a,maxnum):
	firstnumber=0
	while (a<=maxnum):
		b=2
		while(b<=int(math.sqrt(a))):
			if(a%b==0):
				a+=1
				break
			else:
				b+=1
		else :
			firstnumber=a
			break
	return firstnumber;

#修改列表值，将当前素数的倍数索引位置置为0
def changelist(prime,minnumber,maxnumber,list1):
	a=prime
	b=2
	print str(a)+"的倍数索引"
	while(a*b<=maxnumber):
		print "修改索引："+str(a*b)
		if(list1[a*b-minnumber]==1):
			list1[a*b-minnumber]=0
 		b+=1
	return;

print "请输入数组范围"
a=int(raw_input("最小值："))
maxnum=int(raw_input("最大值："))
mida=a
list1=[] #存储maxnum-a个空间大小的数据。数据格式为字典，key为当前值，value为是否是素数，默认为1，说明默认当前值是素数
print "筛选法求素数..."
for i in range(maxnum-a+1):
	list1.append(1)
print "序列默认所有数均为素数：\n"
print list1
if (a<=int(math.sqrt(maxnum))):
	print str(a)+"~"+str(int(math.sqrt(maxnum)))+"之间的素数，开始..."
	while (mida<=int(math.sqrt(maxnum))):
		print str(mida)+"后的第一个素数：\n"
		prime=getprime(mida,maxnum)
		if (prime==0):
			mida+=1
			break
		print prime
		changelist(prime,a,maxnum,list1)
		print "修改后的列表为\n："
		print list1
		mida=prime+1
else:
	while(mida<=maxnum):
		print str(mida)+"后的第一个素数：\n"
		prime=getprime(mida,maxnum)
		if (prime==0):
			mida+=1
			break
		print prime
		changelist(prime,a,maxnum,list1)
		print "修改后的列表为："
		print list1
		mida=prime+1
print "所有的素数："
for i in range(len(list1)):
	if(list1[i]==1):
		print a+i