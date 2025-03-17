from turtle import *

def teglalap():
    begin_fill()
    forward(400)
    left(90)
    forward(150)
    left(90)
    forward(400)
    left(90)
    forward(150)
    end_fill()    

reset()
color("gold")
fillcolor("white")
teglalap()
up()
forward(150)
left(90)
down()
fillcolor("red")
teglalap()


