def fakt(n):
    if n > 1:
        return int(n * fakt(n-1))
    else:
        return 1
        
print(fakt(4))
