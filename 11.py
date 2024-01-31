import turtle as t
t.bgcolor('black')
t.pencolor('red')
t.pensize('2')
t.speed(0)
for i in range(140):
    t.fd(120)
    t.rt(60)
    t.backward(190 + i)
    t.fd(70)
    
t.pencolor('orange')
t.pensize("2") 
t.speed(0)   
for i in range(100):
    t.goto(80, 650)
    t.fd(120)
    t.circle(20 + i)
    t.lt(60)
    t.rt(10)
    
t.pencolor('yellow')
t.pensize('2')
t.speed(0)
for i in range(100):
    t.goto(-320, 380)
    t.backward(120)
    t.rt(60)
    t.fd(120 + i)
    
t.pencolor("cyan")
t.pensize('2')
t.speed(0)
for i in range(100):
    t.goto(-280, -380)
    t.fd(120)
    t.rt(80)
    t.fd(40 + i)
    t.circle(20)
    t.backward(90)
    
t.pencolor("pink")
t.pensize('2')  
t.speed(0)  
for i in range(110):
    t.goto(120, -780)
    t.backward(1 + i)
    t.lt(70)
    t.backward(10)
    t.circle(5 + i)
    t.rt(40 )
t.done()

#copyright 
#Made by @AADI
#unique graphic gui
    