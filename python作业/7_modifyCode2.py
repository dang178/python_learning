#__*__coding:utf-8__*__
import random
num1=random.randint(1,100)
num2=random.randint(1,100)
sums=num1+num2
diff=num1-num2
pro=num1*num2
print(str(num1)+"+"+str(num2)+"="+str(sums))
print(str(num1)+"-"+str(num2)+"="+str(diff))
print(str(num1)+"*"+str(num2)+"="+str(pro))
if(num2!=0):
    quot=num1/num2
    print(str(num1)+"/"+str(num2)+"="+str(quot))
    remainder=num1//num2
    print(str(num1)+"%"+str(num2)+"="+str(remainder))
