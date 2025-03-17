from random import randrange
fi = ""
n = int(input("Hány dobás legyen? "))
for i in range(n):
    if randrange(0,2) == 0:
        fi += 'F'
    else:
        fi += 'I'
print(fi)
ex = ""
i = 0
while i <= n and fi.find(ex) > -1:
    ex = ""
    for j in range(i+1):
        ex += 'I'
    i += 1
print("\nÍrás a legtöbbször egymás után ennyiszer: ", i - 1)
