a = float(input("Kérem a háromszög egyik oldalát: "))
b = float(input("Kérem a háromszög másik oldalát: "))
c = float(input("Kérem a háromszög harmadik oldalát: "))
if a + b > c and a + c > b and b + c > a:
    print("szerkeszthető háromszög")
else:
    print("nem szerkeszthető háromszög")
