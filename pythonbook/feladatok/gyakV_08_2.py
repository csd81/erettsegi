from random import randrange

#a) feladat
class Cars():
    pass
car = []
for i in range(10):
    car.append(Cars())

#b) feladat
brands = ["BMW","Fiat","Volvo","Peugeot"]
colors = ["fekete","kék","fehér","zöld"]
for i in range(10):
    lpn = ""
    for j in range(3):
        lpn += chr(randrange(65,91))
    lpn +='-'
    for j in range(3):
        lpn += chr(randrange(48,58))        
    car[i].num = lpn
    car[i].br = brands[randrange(4)]
    car[i].co = colors[randrange(4)]
    car[i].year = randrange(2010,2020)
    car[i].pr = 1000 * randrange(8,16)
    
#c) feladat    
for i in range(10):
    print(car[i].num, car[i].br, car[i].year \
          , car[i].co, car[i].pr)
print()

#d) feladat
for i in range(10):
    print("rendszám: %s, évjárat: %d, kor: %d év" % \
          (car[i].num, car[i].year, 2020-car[i].year))
print()

#e) feladat
sum = 0
for i in range(10):
    sum += car[i].pr
print("Összérték: ", sum)
