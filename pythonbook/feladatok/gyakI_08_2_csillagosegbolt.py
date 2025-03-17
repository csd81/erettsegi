from turtle import *
from random import randrange

reset()
bgcolor("black")
color("white")
for i in range(50):
    x = randrange(-300,310)
    y = randrange(-200,210)
    up()
    goto(x,y)
    down()
    for i in range(10):
        forward(5)
        backward(5)
        left(36)
    


