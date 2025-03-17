f = input("Kérem az első ötbetűs szót: ")
s = input("Kérem a második ötbetűs szót: ")
if f[1:4] > s[1:4]:
    print(s, f)
else:
    print(f, s)
