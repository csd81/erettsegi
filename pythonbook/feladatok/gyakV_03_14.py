from random import randrange
bs = ""
for i in range(20):
    v = randrange(0,4)
    if v == 0:
        bs += 'A'
    elif v == 1:
        bs += 'C'
    elif v == 2:
        bs += 'G'
    else:
        bs += 'T'
print(bs)
