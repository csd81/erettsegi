a = int(input("Kérek egy egész számot: "))
i = 2
while not(int(a / i) == 1 and a % i == 0):
    if a % i == 0:
        a = a / i
        print(i,"*",end="",sep="")
    else:
        i+=1
print(i,"*1",sep="")
