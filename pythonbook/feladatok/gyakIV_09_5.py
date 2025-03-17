print("   ",end="")
for i in range(1,51):
    print(int(i / 10), end="")
print("")
print("   ",end="")
for i in range(1,51):
    print(i % 10, end="")
print("")
for i in range(1,51):
    print("%d%d " %(int(i/10),i % 10), end="")
    for j in range(1, 51):    
        if i % 2 == 1 and j % 2 ==1 or i % 2 == 0 and j % 2 ==0:
            print("B", end="")
        else:
            print("W", end="") 
    print("")
