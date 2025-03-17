character = [[' ',' ',' ','A','A',' ',' ',' '],
             [' ',' ','A','A','A','A',' ',' '],
             [' ','A','A',' ',' ','A','A',' '],
             ['A','A',' ',' ',' ',' ','A','A'],
             ['A','A','A','A','A','A','A','A'],
             ['A','A','A','A','A','A','A','A'],
             ['A','A',' ',' ',' ',' ','A','A'],
             ['A','A',' ',' ',' ',' ','A','A']]

def chout(c):
    for i in range(8):
        for j in range(8):
            print(c[i][j], sep = "", end = "")
        print()
    print('\n')

def mirror(mc):
    for i in range(4):
        for j in range(8):
            buff = mc[i][j]
            mc[i][j] = mc[7-i][j]
            mc[7-i][j] = buff

chout(character)
mirror(character)
chout(character)
