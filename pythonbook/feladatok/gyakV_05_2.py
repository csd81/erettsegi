from random import randrange
table = []
for i in range(0,8):
    row = []
    for j in range(0,8):
        row.append(0)
    table.append(row)
for k in range(1,4):
    i = randrange(0,8)
    j = randrange(0,8)
    while table[i][j] != 0:
        i = randrange(0,8)
        j = randrange(0,8)
    table[i][j] = k
fig = ['.','K', 'B', 'k']
for i in range(0,8):
    for j in range(0,8):
        print(fig[table[i][j]], sep="", end="")
    print()
