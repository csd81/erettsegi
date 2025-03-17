from turtle import *
from random import randrange

reset()
szin = ["red","orange","yellow","green","blue","purple"]
x = 200
for j in range(6):
    y = randrange(6)
    color(szin[y])
    fillcolor(szin[y])
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

