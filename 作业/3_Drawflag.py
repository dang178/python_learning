import time
import turtle
import os
def draw_rectangle(start_x,start_y,rec_x,rec_y):
    turtle.goto(start_x,start_y)
    turtle.color('red')
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(rec_x)
        turtle.left(90)
        turtle.forward(rec_y)
        turtle.left(90)
    turtle.end_fill()

def draw_star(center_x,center_y,radius):
    turtle.setpos(center_x,center_y)
    #find the peak of the five-pointed star
    pt1=turtle.pos()
    turtle.circle(-radius,72)
    pt2=turtle.pos()
    turtle.circle(-radius,72)
    pt3=turtle.pos()
    turtle.circle(-radius,72)
    pt4=turtle.pos()
    turtle.circle(-radius,72)
    pt5=turtle.pos()
    #draw the five-pointed star
    turtle.color('yellow','yellow')
    #turtle.fill(True)
    turtle.begin_fill()
    turtle.goto(pt3)
    turtle.goto(pt1)
    turtle.goto(pt4)
    turtle.goto(pt2)
    turtle.goto(pt5)
    #turtle.fill(False)
    turtle.end_fill()

turtle.speed(5)
turtle.penup()
#画矩形
star_x=-320
star_y=-260
len_x=660
len_y=440
draw_rectangle(star_x,star_y,len_x,len_y)
#画大五角星
pice=660/30
big_center_x=star_x+5*pice
big_center_y=star_y+len_y-pice*5
turtle.goto(big_center_x,big_center_y)
turtle.left(90)
turtle.forward(pice*3)
turtle.right(90)
draw_star(turtle.xcor(),turtle.ycor(),pice*3)
#画第一个小五角星
turtle.goto(star_x+10*pice,star_y+len_y-pice*2)
turtle.left(turtle.towards(big_center_x,big_center_y)-turtle.heading())
turtle.forward(pice)
turtle.right(90)
draw_star(turtle.xcor(),turtle.ycor(),pice)
#画第二个五角星
turtle.goto(star_x+pice*12,star_y+len_y-pice*4)
turtle.left(turtle.towards(big_center_x,big_center_y)-turtle.heading())
turtle.forward(pice)
turtle.right(90)
draw_star(turtle.xcor(),turtle.ycor(),pice)
#画第三个五角星
turtle.goto(star_x+pice*12,star_y+len_y-7*pice)
turtle.left(turtle.towards(big_center_x,big_center_y)-turtle.heading())
turtle.forward(pice)
turtle.right(90)
draw_star(turtle.xcor(),turtle.ycor(),pice)
#画第四个五角星
turtle.goto(star_x+pice*10,star_y+len_y-9*pice)
turtle.left(turtle.towards(big_center_x,big_center_y)-turtle.heading())
turtle.forward(pice)
turtle.right(90)
draw_star(turtle.xcor(),turtle.ycor(),pice)
turtle.ht()
time.sleep(30)
os._exit(1)
