change = {'0': "0000",'1': "0001", '2': "0010",'3': "0011",
          '4': "0100",'5': "0101",'6': "0110",'7': "0111",
          '8': "1000",'9': "1001",'A': "1010",'B': "1011",
          'C': "1100",'D': "1101",'E': "1110",'F': "1111"}
#1. feladat
v = input("A szám a 16-osban: ")
v = v.upper()
print("Ugyanez a 2-esben: ")
for i in range(len(v)):
    print(change[v[i]], end='')
print()
#2. feladat
revch = {}
for key in change:
    revch[change[key]] = key  
for rkey in revch:
    print (rkey, revch[rkey])
#3. feladat
b = input("Kérek egy 8 bites 2-es számrendszerbeli számot: ")
print(revch[b[0:4]],revch[b[4:8]], sep='')
