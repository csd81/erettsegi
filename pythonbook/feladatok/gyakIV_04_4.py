y = int(input("Kérek egy évszámot (1870..1930): "))
if y % 4 == 0 and y % 100 != 0:
    print("Szökőév.")
else:
    print("Nem szökőév.")
