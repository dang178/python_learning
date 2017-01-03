import time
import turtle
import math
def draw_rectangle(start_x,start_y,rec_x,rec_y):
	turtle.up()
	turtle.goto(start_x,start_y)
	turtle.fillcolor('#EEC211')
	turtle.pencolor('black')
	turtle.pensize(1)
	turtle.down()
	turtle.begin_fill()
	for i in range(2):
		turtle.forward(rec_x)
		turtle.left(90)
		turtle.forward(rec_y)
		turtle.left(90)
	turtle.end_fill()
#上三角米字
def draw_mirect_1(cur_x,cur_y,len_x,len_y):
        #画中间的米字
        #turtle.up()
        #turtle.goto(star_x+3*len_x,star_y+len_y)
        turtle.fillcolor('#EEC211')
        turtle.pencolor('black')
        turtle.pensize(1)
        #turtle.down()
        turtle.begin_fill()
        turtle.forward(len_x*2)
        turtle.left(135)
        turtle.forward(math.sqrt(len_x*len_x+len_y*len_y))
        turtle.right(135)
        turtle.forward(len_x)
        turtle.right(90)
        turtle.forward(len_y)
        turtle.left(90)
        turtle.forward(len_x)
        turtle.left(90)
        turtle.forward(len_y)
        turtle.left(135)
        turtle.forward(math.sqrt(len_x*len_x+len_y*len_y))
        turtle.right(135)
        turtle.forward(len_y)
        turtle.right(90)
        turtle.forward(len_x)
#画米字上三角
def draw_mirect_2(cur_x,cur_y,len_x,len_y):
        turtle.fillcolor('#EEC211')
        turtle.pencolor('black')
        turtle.pensize(1)
        turtle.begin_fill()
        turtle.forward(len_x*2)
        turtle.left(90)
        turtle.forward(len_y)
        turtle.left(135)
        turtle.forward(math.sqrt(len_x*len_x+len_y*len_y))
        turtle.right(135)
        turtle.forward(len_y)
        turtle.right(90)
        turtle.forward(len_x)
        turtle.right(45)
        turtle.forward(math.sqrt(len_x*len_x+len_y*len_y))
        turtle.left(135)
        turtle.forward(len_y)
        turtle.left(90)
        turtle.forward(len_x*2)
        turtle.left(90)
        turtle.forward(len_y)
        turtle.left(90)
        turtle.forward(len_x*2)
        
#draw the rectangle
star_x=-320
star_y=260
len_x=40
len_y=40
#画第一行
turtle.hideturtle()
for i in range(0,3):
	draw_rectangle(star_x+i*len_x,star_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
draw_mirect_1(cur_x,cur_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
turtle.goto(cur_x,cur_y-len_y)
(cur_x,cur_y)=turtle.pos()
for i in range(0,3):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
#画第二行
turtle.up()
turtle.goto(star_x,star_y-len_y)
turtle.down()
(cur_x,cur_y)=turtle.pos()
for i in range(0,3):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
draw_mirect_2(cur_x,cur_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
for i in range(0,3):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y) 
#画第三行
turtle.up()
turtle.goto(star_x,star_y-len_y*2)
turtle.down()
(cur_x,cur_y)=turtle.pos()
for i in range(0,8):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
#画第四行
turtle.up()
turtle.goto(star_x,star_y-len_y*3)
turtle.down()
(cur_x,cur_y)=turtle.pos()
for i in range(0,8):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
#画第五行
turtle.up()
turtle.goto(star_x,star_y-len_y*3)
turtle.down()
(cur_x,cur_y)=turtle.pos()
turtle.right(90)
turtle.forward(len_y)
turtle.write("                楚河                汉界",font=("微软雅黑", 14, "normal"))
turtle.left(90)
turtle.forward(len_x*8)
turtle.left(90)
turtle.forward(len_y)
turtle.right(90)
#画下半部分
turtle.up()
turtle.goto(star_x,star_y-len_y*5)
turtle.down()
(cur_x,cur_y)=turtle.pos()
for i in range(0,8):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
#画第六行
turtle.up()
turtle.goto(star_x,star_y-len_y*6)
turtle.down()
(cur_x,cur_y)=turtle.pos()
for i in range(0,8):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
#画第七行
turtle.up()
turtle.goto(star_x,star_y-len_y*7)
turtle.down()
(cur_x,cur_y)=turtle.pos()
for i in range(0,3):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
draw_mirect_1(cur_x,cur_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
turtle.goto(cur_x,cur_y-len_y)
(cur_x,cur_y)=turtle.pos()
for i in range(0,3):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
#画第八行
turtle.up()
turtle.goto(star_x,star_y-len_y*8)
turtle.down()
(cur_x,cur_y)=turtle.pos()
for i in range(0,3):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
draw_mirect_2(cur_x,cur_y,len_x,len_y)
(cur_x,cur_y)=turtle.pos()
for i in range(0,3):
        draw_rectangle(cur_x+i*len_x,cur_y,len_x,len_y)
turtle.speed(20)
turtle.penup()
turtle.ht()
time.sleep(3)
