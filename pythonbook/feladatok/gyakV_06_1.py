from random import randrange

def strout(ocode):
    for i in ocode:
        print(i, end=' ')
    print()
    
def gen(c):
    gcode =""
    for i in range(c):
        rnd = randrange(0,10)
        gcode += str(rnd)
    return gcode

def shiftleft(scode):
    n = len(scode)
    ncode = ""
    buff = scode[0]
    for i in range(1,n):
        ncode += scode[i]
    ncode += buff
    return ncode

code = gen(5)
strout(code)
code = shiftleft(code)
strout(code)
            
