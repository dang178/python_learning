#__*__coding:utf-8__*__
import math
while(1==1):
    a=float(input("请输入三角形第一个边长:"))
    b=float(input("请输入三角形第二个边长:"))
    c=float(input("请输入三角形第三个边长:"))
    if(a+b>c and a+c>b and b+c>a and a-b<c and a-c<b and b-c<a):
        cos_BC=(b*b+c*c-a*a)/(2*b*c)
        cos_AC=(a*a+c*c-b*b)/(2*a*c)
        angle_BC=math.acos(cos_BC)
        angle_AC=math.acos(cos_AC)
        angle_AB=180-angle_BC-angle_AC
        print("bc夹角分别为："+str(angle_BC)+",ac夹角为："+str(angle_AC)+",ab夹角为：\
"+str(angle_AB))
        break
    else:
        print("输入的三边构不成三角形。")
