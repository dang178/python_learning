import time
import turtle
import math
def draw_rectangle(start_x,start_y,rec_x,rec_y,rect):
	turtle.up()
	turtle.goto(start_x,start_y)
	turtle.fillcolor('#EEC211')
	turtle.pencolor('black')
	turtle.pensize(1)
	turtle.down()
	turtle.begin_fill()
	for i in range(rect):
		turtle.forward(rec_x)
		turtle.left(90)
		turtle.forward(rec_y)
		turtle.left(90)
	turtle.end_fill()

turtle.speed(5)
turtle.penup()
#draw the rectangle
star_x=-320
star_y=260
len_x=40
len_y=40
#画第一行三个矩形
for i in range(0,3):
	draw_rectangle(star_x+i*len_x,star_y,len_x,len_y,2)
#画中间的米字
turtle.up()
turtle.goto(star_x+3*len_x,star_y+len_y)
turtle.fillcolor('#EEC211')
turtle.pencolor('black')
turtle.down()
turtle.begin_fill()
turtle.forward(len_y)
turtle.right(90)
turtle.forward(len_x)
turtle.left(-135)
turtle.forward(math.sqrt(len_x*len_x+len_y*len_y))


turtle.ht()
time.sleep(3)