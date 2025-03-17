a = int(input("Kérem az egyik egészet: "))
b = int(input("Kérem a másik egészet: "))
while a > 0 and b > 0:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print("A legnagyobb közös osztó: ", a)
    a = int(input("Kérem az egyik egészet: "))
    b = int(input("Kérem a másik egészet: "))
