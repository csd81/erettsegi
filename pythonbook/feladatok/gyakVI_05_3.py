maxw = ""
maxl = 0
inp = open("szoveg.txt",'r')
line = inp.readline()
while line != "":
    line = line.strip()
    if len(line) > maxl:
        maxl = len(line)
        maxw = line
    line = inp.readline()
inp.close()
print("Leghosszabb szó: ", maxw, ", hossza: ", maxl)
    
