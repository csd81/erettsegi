inp = open("szoveg.txt",'r')
line = inp.readline()
while line != "":
    line = line.strip()
    print(line, len(line), line[len(line)-1])
    line = inp.readline()
inp.close()
