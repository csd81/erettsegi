r, g, b = [], [], []
re = open("kep.txt",'r')
for i in range(50):
    rowr, rowg, rowb = [], [], []
    for j in range(50):
        line = re.readline()
        line = line.strip()
        datas = line.split()
        rowr.append(int(datas[0]))
        rowg.append(int(datas[1]))
        rowb.append(int(datas[2]))
    r.append(rowr)
    g.append(rowg)
    b.append(rowb)
re.close()
print("   ", end="")
for i in range(50):
    print(int(i/10), sep="", end="")
print()
print("   ", end="")
for i in range(50):
    print(i % 10, sep="", end="")    
print()
for i in range(50):
    print("%d%d " %(int(i / 10), i % 10), end="")
    for j in range(50):
        if r[i][j] == 255 and g[i][j] == 0 and b[i][j] == 0:
            print('P', sep = "", end="")
        elif r[i][j] == 0 and g[i][j] == 255 and b[i][j] == 0:
            print('Z', sep = "", end="")
        elif r[i][j] == 0 and g[i][j] == 0 and b[i][j] == 255:
            print('K', sep = "", end="")
        elif r[i][j] == 255 and g[i][j] == 255 and b[i][j] == 0:
            print('S', sep = "", end="")
        else:
            print('.', sep = "", end="")
    print()


