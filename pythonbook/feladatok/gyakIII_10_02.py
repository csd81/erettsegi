a = int(input("Kérek egy háromjegyű egészt: "))
e = a % 10
sz = int(a / 100)
t = int(a % 100 / 10)
print ("A %d egyesei: %d, tízesei: %d, százasai: %d" % (a, e, t, sz))
