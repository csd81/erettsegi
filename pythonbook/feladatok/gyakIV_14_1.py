def lnko(a,b):
    if a == b :
        return a
    elif a < b:
        return lnko(a, b-a)
    else:
        return lnko(a-b, b)

print(lnko(120,200))
