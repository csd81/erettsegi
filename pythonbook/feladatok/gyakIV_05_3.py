w1 = input("Kérek egy szót: ")
w2 = input("Kérek egy másik szót: ")
w3 = input("Kérek egy harmadik szót: ")
if w1 > w2:
    if w1 < w3:
        print(w2, w1, w3)
    else:
        if w2 > w3:
            print(w3, w2, w1)
        else:
            print(w2, w3, w1)
else:
    if w3 > w2:
        print(w1, w2, w3)
    else:
        if w1 > w3:
            print(w3, w1, w2)
        else:
            print(w1, w3, w2)

