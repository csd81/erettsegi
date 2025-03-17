a = int(input("Kérem egy egész számot: "))
i = 2
while i * i < a and a % i != 0:
    i += 1
if a % i == 0:
    print("nem prím")
else:
    print("prím")
