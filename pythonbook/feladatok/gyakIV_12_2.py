def hminsec(h, m, s):
    print("%d:" % (h), end='')
    if m < 10:
        print('0', end='')
    print("%d:" % (m), end='')
    if s < 10:
        print('0', end='')
    print(s)

def sectohminsec(sec):
    ho = int(sec / 3600)
    mo = sec % 3600
    mi = int(mo / 60)
    se = mo % 60
    hminsec(ho, mi, se)
    

s = int(input("Kérek egy másodperc adatot: "))
sectohminsec(s)
