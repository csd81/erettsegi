from turtle import *
from random import randrange

reset()
y = 200
for i in range(100):
    x = randrange(0,360,90)
    while x == y:
        x = randrange(0,360,90)    
    right(x)
    forward(25)
    y = x
    


