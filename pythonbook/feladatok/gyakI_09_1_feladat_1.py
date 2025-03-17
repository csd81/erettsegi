from turtle import *

szin = ["red", "orange", "yellow", "green", "blue", 
        "red", "orange", "yellow", "green", "blue"]
reset()
for j in range(10):
    color(szin[j])
    right(36)
    forward(200)
    right(45)
    fillcolor(szin[j])
    begin_fill()
    for i in range(4):
        forward(20)
        left(90)
    end_fill()
    left(45)
    backward(200)
