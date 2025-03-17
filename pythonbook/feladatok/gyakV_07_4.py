edgem = {(1,2) : 1, (1,3) : 2, (2,1) : 1, (5,2) : 4,
         (1,4) : 1, (2,5) : 2, (4,1) : 2, (3,4) : 1}
print("  ", end='')
for i in range(1,6):
    print(i, end = '')
print('\n')
for i in range(1,6):
    print("%d " % (i), end='')
    for j in range(1,6):
        print(edgem.get((i,j),'0'),end='')
    print()
