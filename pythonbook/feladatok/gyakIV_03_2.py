from math import sqrt
a = float(input("Kérem a másodfokú tag együtthatóját: "))
b = float(input("Kérem az elsőfokú tag együtthatóját: "))
c = float(input("Kérem az állandót: "))
D = b * b - 4 * a * c
if D < 0:
    print("Nincs megoldás.")
elif D == 0:
    print("A megoldás: ", -b / (2 * a))
else:
    print("Az egyik megoldás: ", (-b+sqrt(D))/(2 * a))
    print("Az másik megoldás: ", (-b-sqrt(D))/(2 * a))
