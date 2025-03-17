from turtle import *

reset()

def negyzet(y,i):
    if i > 0:
        forward(y)
        right(90)
        negyzet(y, i - 1)

def alakzat(x):
    if x > 30:
        negyzet(x, 4)
        forward(x / 2)
        right(45)
        x = 1.41 * x / 2
        alakzat(x)

alakzat(200)
