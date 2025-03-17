from turtle import *
from random import randrange

def teglalap(x,y):
    begin_fill()
    forward(x)
    left(90)
    forward(y)
    left(90)
    forward(x)
    left(90)
    forward(y)
    end_fill()

def trikolor(f, k, a):
    fillcolor(f)
    teglalap(400,100)
    up()
    forward(100)
    left(90)
    down()
    fillcolor(k)
    teglalap(400,100)
    up()
    forward(100)
    left(90)
    down()
    fillcolor(a)
    teglalap(400,100)
    left(90)

def dikolor(felso, also):
    fillcolor(felso)
    teglalap(400,150)
    up()
    forward(150)
    left(90)
    down()
    fillcolor(also)
    teglalap(400,150)
    left(90)

def ftrikolor(b, k, j):
    fillcolor(b)
    teglalap(133,300)
    up()
    left(90)
    forward(133)
    down()
    fillcolor(k)
    teglalap(133,300)
    up()
    left(90)
    forward(133)
    down()
    fillcolor(j)
    teglalap(133,300)
    left(90)

def zaszlo(nemzet):
    if nemzet == "magyar":
        trikolor("red","white","green")
    elif nemzet == "osztrak":
        trikolor("red","white","red")
    elif nemzet == "nemet":
        trikolor("black","red","yellow")
    elif nemzet == "holland":
        trikolor("red","white","blue")
    elif nemzet == "jemeni":
        trikolor("red","white","black")
    elif nemzet == "orosz":
        trikolor("white","blue","red")
    elif nemzet == "olasz":
        ftrikolor("green","white","red")
    elif nemzet == "nigeriai":
        ftrikolor("green","white","green")
    elif nemzet == "lengyel":
        dikolor("white","red")
    elif nemzet == "monacoi":
        dikolor("red","white")
    else:
        trikolor("white","white","white")

reset()
n = ["magyar", "osztrak","nemet","holland","jemeni",
    "orosz","olasz","nigeriai","lengyel","monacoi"]
color("gold")
x = randrange(10)
zaszlo(n[x])


