tav = int(input("Kérek egy távolságot (1 - 30)"))
if tav < 3:
    ossz = 500
elif tav < 6:
    ossz = 700
elif tav < 11:
    ossz = 900
elif tav < 21:
    ossz = 1400
else:
    ossz = 2000
print("Dijazás: ", ossz)
