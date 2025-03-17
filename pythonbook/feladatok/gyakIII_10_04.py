sz1 = int(input("Kérem az első tört számlálóját: "))
n1 = int(input("Kérem az első tört nevezőjét: "))
sz2 = int(input("Kérem a második tört számlálóját: "))
n2 = int(input("Kérem a második tört nevezőjét: "))
kn = n1 * n2
szu1,szu2 = sz1*kn/n1,sz2*kn/n2
esz = szu1 + szu2
print ("%d/%d + %d/%d = %d/%d + %d/%d = %d/%d" % \
       (sz1,n1,sz2,n2,szu1,kn,szu2,kn,esz,kn))
