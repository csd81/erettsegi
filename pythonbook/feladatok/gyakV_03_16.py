from math import pow

chng = [["I","II","III","IV","V","VI","VII","VIII","IX"],
        ["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
        ["C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
        ["M","MM","MMM"]]

v = int(input("Kérem az átváltandó számot: "))
r = ""
for i in range(3,-1,-1):
    b = int( v / pow(10,i))
    if b != 0:
        r += chng[i][b - 1]
    v = v % pow(10,i)
print("A római szám: ", r)

          
