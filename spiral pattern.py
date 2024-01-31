from turtle import *
colors=["red", "orange", "pink", "cyan", "yellow", "white"]
speed(100)
bgcolor("black")
for x in range(1200):
    color(colors[x%6])
    forward(x*.5)
    left(149)
