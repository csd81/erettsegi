a = int(input("Kérem az egyik egészet: "))
b = int(input("Kérem a másik egészet: "))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print("A legnagyobb közös osztó: ", a)
