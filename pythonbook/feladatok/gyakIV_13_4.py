def kmtoft(km):
    if km <= 2:
        return 500
    elif km <= 5:
        return 700
    elif km <= 10:
        return 900
    elif km <= 20:
        return 1400
    else:
        return 2000

print(kmtoft(9))
