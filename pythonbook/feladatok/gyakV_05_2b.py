from random import randrange

table = []
for i in range(0,8):
    row = []
    for j in range(0,8):
        row.append(0)
    table.append(row)
for k in range(1,3):
    i = randrange(0,8)
    j = randrange(0,8)
    while table[i][j] != 0:
        i = randrange(0,8)
        j = randrange(0,8)
    table[i][j] = k
i = randrange(0,8)
j = randrange(0,8)
b = 1
while not(table[i][j] == 0 and b == 0):
    b = 0
    for m in range(-1,2):
        for l in range(-1,2):
            if 0 <= i + m <= 7 and 0 <= j + l <= 7:
                if table[i+m][j+l] == 1:
                    b = 1
    if b == 1 or table[i][j] !=0:
        i = randrange(0,8)
        j = randrange(0,8)
table[i][j] = 3                    
fig = ['.','K', 'B', 'k']
for i in range(0,8):
    for j in range(0,8):
        print(fig[table[i][j]], sep="", end="")
    print()
