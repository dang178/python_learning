# --*-- coding:UTF-8 --*--
import sys
import math

##���a~maxnum֮���һ������
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

#�޸��б�ֵ������ǰ�����ı�������λ����Ϊ0
def changelist(prime,minnumber,maxnumber,list1):
	a=prime
	b=2
	print str(a)+"�ı�������"
	while(a*b<=maxnumber):
		print "�޸�������"+str(a*b)
		if(list1[a*b-minnumber]==1):
			list1[a*b-minnumber]=0
 		b+=1
	return;

print "���������鷶Χ"
a=int(raw_input("��Сֵ��"))
maxnum=int(raw_input("���ֵ��"))
mida=a
list1=[] #�洢maxnum-a���ռ��С�����ݡ����ݸ�ʽΪ�ֵ䣬keyΪ��ǰֵ��valueΪ�Ƿ���������Ĭ��Ϊ1��˵��Ĭ�ϵ�ǰֵ������
print "ɸѡ��������..."
for i in range(maxnum-a+1):
	list1.append(1)
print "����Ĭ����������Ϊ������\n"
print list1
if (a<=int(math.sqrt(maxnum))):
	print str(a)+"~"+str(int(math.sqrt(maxnum)))+"֮�����������ʼ..."
	while (mida<=int(math.sqrt(maxnum))):
		print str(mida)+"��ĵ�һ��������\n"
		prime=getprime(mida,maxnum)
		if (prime==0):
			mida+=1
			break
		print prime
		changelist(prime,a,maxnum,list1)
		print "�޸ĺ���б�Ϊ\n��"
		print list1
		mida=prime+1
else:
	while(mida<=maxnum):
		print str(mida)+"��ĵ�һ��������\n"
		prime=getprime(mida,maxnum)
		if (prime==0):
			mida+=1
			break
		print prime
		changelist(prime,a,maxnum,list1)
		print "�޸ĺ���б�Ϊ��"
		print list1
		mida=prime+1
print "���е�������"
for i in range(len(list1)):
	if(list1[i]==1):
		print a+i