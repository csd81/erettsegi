a = float(input("A helyiség hosszúsága: "))
b = float(input("A helyiség szélessége: "))
x = float(input("A burkolólap hosszúsága: "))
y = float(input("A burkolólap szélessége: "))
tsz = a * b
tb = x * y
db = int(1.2 * tsz / tb) + 1
print("A szükséges burkolólapok száma: ", db)
