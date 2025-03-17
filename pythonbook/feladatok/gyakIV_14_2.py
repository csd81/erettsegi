def lnko(a,b):
    if a == b :
        return a
    elif a < b:
        return lnko(a, b-a)
    else:
        return lnko(a-b, b)

def lkkt(a,b):
    return int(a * b / lnko(a , b))
    
print(lkkt(120,200))
