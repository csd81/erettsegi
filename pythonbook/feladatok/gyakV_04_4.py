def timetosec(time):
    fcts = time.split(':')
    h = int(fcts[0])
    m = int(fcts[1])
    s = int(fcts[2])
    s = s + h * 3600 + m * 60
    return s

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
    
time1 = input("Kérem az egyik időpontot: ")
time2 = input("Kérem a másik időpontot: ")
diff = timetosec(time1) - timetosec(time2)
if diff < 0:
    diff = -1 * diff
print("A különbség: ",end ='')
sectohminsec(diff)

