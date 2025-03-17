nap = int(input("Kérem a nap sorszámát: "))
ra = int(input("Kérem a rádióamatőr sorszámát: "))
inp = open("veetel.txt",'r')
line1 = inp.readline()
line2 = inp.readline()
talalt = False
while line1 != "" and line2 !="" and not(talalt):
    line1, line2 = line1.strip(), line2.strip()
    num = line1.split()
    if int(num[0]) == nap and int(num[1]) == ra:
        talalt = True
        mes = line2.split()
        if mes[0].find("#") > -1 or not('9' >= line2[0] >= '0'):
            print("Nincs információ")
        else:
            fox = mes[0].split('/')
            print("A megfigyelt egyedek száma: ", int(fox[0]) + int(fox[1]))
    line1, line2 = inp.readline(), inp.readline()
if not(talalt):
    print("Nincs ilyen feljegyzés")
inp.close()
