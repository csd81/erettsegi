from random import randrange
def gen(num):
    for i in range(num):
        print(randrange(0,10) , end='')
    print()

n = int(input("Hány jegyű legyen a számvariáció? "))
gen(n)
