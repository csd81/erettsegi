def fns(num1,num2):
    end1 = int(num1/2)
    s1 = 1
    for i in range(2,end1+1):
        if num1 % i == 0:
            s1 += i
    end2 = int(num2/2)
    s2 = 1
    for i in range(2,end2+1):
        if num2 % i == 0:
            s2 += i          
    if s1 == num2 and s2 == num1:
        print("Barátságos számpár")
    else:
        print("Nem barátságos számpár")

ob1 = int(input("Kérem az egyik vizsgálandó számot: "))
ob2 = int(input("Kérem a másik vizsgálandó számot: "))
fns(ob1,ob2)
        
