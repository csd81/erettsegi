from random import randrange
rn = randrange(6)+1
if rn == 1:
    print("")
    print(" * ")
    print("")
elif rn == 2:
    print("*")
    print("")
    print("  *")
elif rn == 3:
    print("*")
    print(" *")
    print("  *")
elif rn == 4:
    print("* *")
    print(" ")
    print("* *")
elif rn == 5:
    print("* *")
    print(" *")
    print("* *")
else:
    print("***")
    print(" ")
    print("***")
