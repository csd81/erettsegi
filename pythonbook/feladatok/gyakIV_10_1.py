a = int(input("Kérem az egyik pozitív egészet: "))
while a <= 0:
    a = int(input("Kérem az egyik pozitív egészet: "))

b = int(input("Kérem a másik pozitív egészet: "))
while b <= 0:
    b = int(input("Kérem a másik pozitív egészet: "))

c = a
d = b
while c != d:
    if c > d:
        d += b
    else:
        c += a
print("A legkisebb közös többszörös: ", c)
