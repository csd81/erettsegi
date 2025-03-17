sz = int(input("Kérem a tört számlálóját: "))
n = int(input("Kérem a tört nevezőjét: "))
if sz % n == 0:
    print(sz/n)
else:
    print("nem egész")
