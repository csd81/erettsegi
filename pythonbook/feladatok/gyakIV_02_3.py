a = int(input("Kérek egy háromjegyű egész számot: "))
sz = int(a / 100)
t = int((a % 100) / 10)
e = a % 10
if a == sz*sz*sz+t*t*t+e*e*e:
    print("Amstrong-szám")
else:
    print("Nem Amstrong-szám")
    
