from random import randrange
rnd = []
for i in range(10):
    rnd.append(randrange(1,7))
i = 0    
while i < 10 and rnd[i] != 6:
    i += 1
if i >= 10:
    print("Nincs benne 6-os")
else:
    print("Van benne 6-os")
for i in range(10):
    print(rnd[i], end=' ')
