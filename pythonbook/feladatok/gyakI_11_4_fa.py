from turtle import *

def fa(x, sz):
    if sz > 0:
        forward(x/2)
        left(30)
        fa(x/2, sz - 1)
        right(60)
        fa(x/2, sz - 1)
        left(30)
        backward(x/2)
    else:
        forward(x)
        backward(x)

left(90)
fa(200,0)
