from random import randrange
t = input("Kérem a tipped fej vagy írás (F/I)")
rnd = randrange(0,2)
if rnd == 0:
    rndc = 'F'
else:
    rndc = 'I'
if t == rndc:
    print("Eltaláltad.")
else:
    print("Nem találtad el.")
