from turtle import *

reset()

x = 200
for j in range(6):
    for i in range(4):
        forward(x)
        right(90)
    forward(x / 2)
    right(45)
    x = 1.41 * x / 2

