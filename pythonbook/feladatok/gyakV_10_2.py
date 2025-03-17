b = []
re = open("bsa.txt",'r')
line = re.readline()
while line != "":
    line = line.strip()
    b.append(line)
    line = re.readline()
re.close()
db = len(b)-1
for i in range(db,-1,-1):
    print(b[i], sep = "", end="")
    
