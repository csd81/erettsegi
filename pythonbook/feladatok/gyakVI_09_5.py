words = []
inp = open("szoveg.txt",'r')
line = inp.readline()
while line != "":
    line = line.strip()
    if len(line) == 5:
        words.append(line)
    line = inp.readline()
inp.close()

n = len(words)
for i in range(n-1):
    for j in range(n-1, i, -1):
        if words[j][1:4] < words[j-1][1:4]:
            words[j], words[j-1] = words[j-1], words[j]
            
out = open("letra.txt","w")  
if words[0][1:4] == words[1][1:4]:
    out.write(words[0]+'\n')
for i in range(1,len(words)-2):
    if words[i][1:4] == words[i-1][1:4] or \
        words[i][1:4] == words[i+1][1:4]:
        out.write(words[i]+'\n')
    if words[i][1:4] != words[i+1][1:4] and \
        words[i][1:4] == words[i-1][1:4]:
        out.write('\n')

if words[i][1:4]==words[i+1][1:4]:
    out.write(words[i+1]+'\n')
out.close()
print("Kész a fájl.")
