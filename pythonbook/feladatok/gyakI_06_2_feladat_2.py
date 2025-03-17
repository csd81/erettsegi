from turtle import *

reset()
up()
goto(-250,+150)
down()
for k in range(18):
    for j in range(25):
        for i in range(4):
            forward(20)
            right(90)
        forward(20)
    backward(500)
    right(90)
    forward(20)
    left(90)
