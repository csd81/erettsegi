word = input("Kérek egy három karakteres szórészletet: ")
inp = open("szoveg.txt",'r')
line = inp.readline()
while line != "":
    line = line.strip()
    if line[1:4] == word and len(line) == 5:
        print(line, end=' ')
    line = inp.readline()
inp.close()

