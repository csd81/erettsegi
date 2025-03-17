a = float(input("Kérem a papír egyik oldalának hosszát: "))
b = float(input("Kérem a papír másik oldalának hoszzát: "))
e = float(input("Kérem a kocka élének hosszát: "))
if a < b:
    a,b = b,a
if a >= 4 * e and b >= 3 * e:
    print("Elkészíthető")
else:
    print("Nem készíthető el")

