for i in range(1,51):
    for j in range(1, 51):    
        if i % 2 == 1 and j % 2 ==1 or i % 2 == 0 and j % 2 ==0:
            print("B", end="")
        else:
            print("W", end="") 
    print("")
