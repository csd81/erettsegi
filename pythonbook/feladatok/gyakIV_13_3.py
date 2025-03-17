def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        a1,a2 = 1,1
        p = 0
        for i in range(0,n-2):
            p = a1 + a2
            a1 = a2
            a2 = p
        return p

for i in range(1,11):
    print(fib(i))
