words = []
inp = open("szoveg.txt",'r')
line = inp.readline()
while line != "":
    line = line.strip()
    words.append(line)
    line = inp.readline()
inp.close()
n = len(words)
for i in range(n-1):
    for j in range(n-1, i, -1):
        if words[j] < words[j-1]:
            words[j], words[j-1] = words[j-1], words[j]
out = open("szavak.txt","w")
for i in range(n):
    out.write(words[i]+' ')
out.close()
print("Kész a fájl.")


    
