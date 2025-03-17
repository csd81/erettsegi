from random import randrange
napok = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]
for i in range(0, 14):
    x = randrange(0,7)
    print(napok[x], end=" ")

