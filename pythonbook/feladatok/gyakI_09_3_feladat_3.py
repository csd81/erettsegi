from turtle import *

reset()
szin = ["red","orange","yellow","green","blue","purple"]
x = 200
for j in range(6):
    color(szin[j])
    fillcolor(szin[j])
    begin_fill()
    for i in range(4):
        forward(x)
        right(90)
    end_fill()
    up()
    forward(x / 2)
    down()
    right(45)
    x = 1.41 * x / 2

