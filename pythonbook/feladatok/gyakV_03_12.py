def hetode(p):
    if 'A' <= p <= 'F':
        return ord(p) - 55
    elif 'a' <= p <= 'f':
        return ord(p) - 87
    else:
        return ord(p) - 48

h = input("Kérek egy kétjegyű, hexadecimális számot: ")
sz = hetode(h[0]) * 16 + hetode(h[1])
print("Tizes számrendszerben: ", sz)
