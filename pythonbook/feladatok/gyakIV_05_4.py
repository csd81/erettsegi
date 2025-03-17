d = int(input("Kérek egy 0 - 255 számot: "))
h0 = d % 16
h1 = int(d / 16)
if h1 <= 9 :
    print(h1,sep='',end='')
else:
    print(chr(h1+55),sep='',end='')
if h0 <= 9 :
    print(h0)
else:
    print(chr(h0+55))
