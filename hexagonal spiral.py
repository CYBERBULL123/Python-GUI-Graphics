import turtle
colors = [
    'red','purple','blue','green','orange','yellow']
t = turtle.Pen()
t.speed(0)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 +  2)
    t.forward(x)
    t.left(49)
