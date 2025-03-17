from turtle import *

reset()
x = 20
for j in range(10):
    right(36)
    forward(x)
    right(45)
    fillcolor("black")
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    left(45)
    backward(x)
    x += 20
