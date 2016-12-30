# __*__coding:utf-8__*__
import sys
weight=float(input("请输入体重(kg)："))
height=float(input("请输入身高(m)："))
BMI=round(weight/(height*height),2)
print("BMI指数："+str(BMI))
