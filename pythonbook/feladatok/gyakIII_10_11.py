from math import sqrt
L = float(input("Kérem a fonál hosszát méterben: "))
P = float(input("Kérem a percek számát: "))
T = 2 * 3.14152 * sqrt(L/9.81)
s = 60 * P # átváltás percről másodpercre
n = int(s/ T)
print("A lengések száma: ", n)
