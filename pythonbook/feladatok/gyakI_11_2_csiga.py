from turtle import *

def csiga(x):
    if x < 210:
        forward(x)
        left(90)
        x+=10
        csiga(x)

csiga(10)

