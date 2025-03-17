from random import randrange
fi = []
n = int(input("Hány dobás legyen? "))
for i in range(n):
    if randrange(0,2) == 0:
        fi.append('F')
    else:
        fi.append('I')
for i in range(n):
    print(fi[i], end='')
#a) feladat
db = 0
for i in range(n):
    if fi[i] == 'F':
        db += 1
print("\nA fejek relatív gyakorisága: %.2f" % (100*(db/n)), end='')
print('%')
#b) feladat
db = 0
if fi[0] == 'F' and fi[1] == 'F' and fi[2] == 'I':
    db += 1
if fi[n-3] == 'I' and fi[n-2] == 'F' and fi[n-1] == 'F':
    db += 1    
for i in range(n-3):
    if fi[i] == 'I'  and fi[i+1] == 'F' and fi[i+2] == 'F' and fi[i+3] == 'I' :
        db += 1
   
print("\nPontosan két fej egymás után ennyiszer: ", db)
