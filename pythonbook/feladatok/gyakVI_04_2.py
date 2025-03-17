from math import sqrt
word = "EEJJJEEBBBEEJEJEJEJEEBBB"
db = 0
for i in range(len(word)-1):
    if word[i] != word[i+1]:
        db += 1
print("Az irányváltások száma: ", db)
x,y = 0,0
for i in range(len(word)):
    if word[i] == 'B':
        x += 1
    elif word[i] == 'J':
        x -= 1
    elif word[i] == 'E':
        y += 1
    else:
        y -= 1
r = sqrt(x*x + y*y)
print("Ilyen távol jutott: ", r)
