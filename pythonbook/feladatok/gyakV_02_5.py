from random import randrange
oldal = ["fej","írás"]
ertek = []
for i in range(0,99):
    ertek.append(randrange(0,2))
for i in range(0,99):
    print(oldal[ertek[i]], end=" ")

# egy alternatív megoldás az utolsó két sor helyett:
print("")
for i in range(0,99):
    if ertek[i] == 0:
        print("fej", end=" ")
    else:
        print("írás", end=" ")
