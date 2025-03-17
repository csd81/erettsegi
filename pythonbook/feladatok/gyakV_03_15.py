#a) feladat
from random import randrange
wlst = ["szelep","nap","informatika","fa","tengely"]
rn = randrange(0, len(wlst))
chw = wlst[rn]
n = len(chw)
print(chw)
#b) feladat
cw = ""
for i in range(0, n):
    cw += 'X'
print(cw)
#c) feladat
c = input("Kérek egy karaktert: ")
for i in range(0, n):
    if chw[i] == c:
        cw = cw[:i] + c + cw[i+1:]
print(cw)
#d) feladat
cw = ""
for i in range(0, n):
    cw += 'X'
print(cw)
db = 0
while db != n:
    c = input("Kérek egy karaktert: ")
    for i in range(0, n):
        if chw[i] == c:
            cw = cw[:i] + c + cw[i+1:]
    db = 0
    for i in range(0, n):
        if cw[i] != 'X':
            db += 1
    print(cw)        
