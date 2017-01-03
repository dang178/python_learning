# __*__coding:utf-8__*__
import xlrd,matplotlib
import os
#获取小格值
def getCellValue(sheet,row_index,col_index):
        return float(sheet.cell(row_index,col_index).value)

data = xlrd.open_workbook("c:\\users\\vlc\\desktop\\学生成绩.xlsx")
sheet1=data.sheet_by_index(0)
nRows=sheet1.nrows
nCols=sheet1.ncols
print("姓名    学号    班级   总分    均分")
#循环每行值
for i in range(1,nRows):
        student_name=str(sheet1.cell(i,1).value)
        student_num=str(round(sheet1.cell(i,0).value,0))
        student_class=str(round(sheet1.cell(i,2).value,0))
        total_Point=0.0
        for j in range(3,nCols):
                total_Point+=getCellValue(sheet1,i,j)
        avg_Point=total_Point/4
        print(student_name+"    "+student_num+"    "+student_class+"   "+str(round(total_Point,2))+"    "+str(round(avg_Point,2)))    
#计算及格率，优良率，优秀率
for i in range(3,nCols):
        passingNum=0
        goodNum=0
        excellentNum=0
        passingRate=0.0
        goodRate=0.0
        excellentRate=0.0
        course=sheet1.cell(0,i).value
        for j in range(1,nRows):
                point=round(getCellValue(sheet1,j,i),2)
                if(point>60):
                        passingNum+=1
                if(point>80):
                        goodNum+=1
                if(point>90):
                        excellentNum+=1
        passingRate=round(passingNum/(nRows-1)*100,2)
        goodRate=round(goodNum/(nRows-1)*100,2)
        excellentRate=round(goodNum/(nRows-1)*100,2)
        print(course+",及格率："+str(passingRate)+"%,优良率："+str(goodRate)+"%,优秀率："+str(excellentRate)+"%")
#画成绩曲线图及直方图
