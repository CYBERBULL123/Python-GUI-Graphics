import turtle
import colorsys
t = turtle.Turtle()
t.pensize(0.1)
t.pencolor("red")
turtle.bgcolor('black')
t.speed(0)   
for i in range(80):
    t.forward(120)
    t.circle(60)
    t.right(80)
    t.goto(-180, 90)
    t.backward(60)
    t.circle(90)
    t.left(160)
    t.circle(80)
    t.fillcolor('red')
    t.penup()
    t.setpos(0, 0)
    t.pendown()
    t.right(21)


