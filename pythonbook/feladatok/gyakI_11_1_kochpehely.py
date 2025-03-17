from turtle import *

def koch(h, sz):
    if sz == 0:
        forward(h)
    else:
        u = int(h/3)
        koch(u, sz-1)
        left(60)
        koch(u, sz-1)
        right(120)
        koch(u, sz-1)
        left(60)
        koch(u, sz-1)

def pehely(oh, fsz):
    koch(oh,fsz)
    right(120)
    koch(oh,fsz)
    right(120)
    koch(oh,fsz)
    right(120)
    
reset()
up()
goto(-300,150)
down()
pehely(500,3)
    
