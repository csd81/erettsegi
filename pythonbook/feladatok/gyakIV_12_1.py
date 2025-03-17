def hminsec(h, m, s):
    print("%d:" % (h), end='')
    if m < 10:
        print('0', end='')
    print("%d:" % (m), end='')
    if s < 10:
        print('0', end='')
    print(s)

ho = int(input("Kérek egy óra adatot: "))
mi = int(input("Kérek egy perc adatot: "))
se = int(input("Kérek egy másodperc adatot: "))
hminsec(ho, mi, se)
