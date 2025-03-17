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

nap = [3,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,5]
fuvar = [3,1,7,2,3,4,5,6,8,9,10,11,1,2,4,5,6,7,8,9,10,11,12,13,14,15,4,1,2,3,5,6,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,17,18,19,1,2,8,3,4,5,6,7,20]
hossz = [10,3,14,3,1,9,5,2,9,8,5,6,7,7,2,4,6,3,5,8,1,4,2,3,5,2,28,11,2,3,7,11,2,5,2,6,2,3,2,6,2,2,4,2,2,4,4,5,2,7,2,3,5,12,25,6,6,6,9,6,7]

for i in range(len(nap)):
    print("%d. nap, %d. fuvar: %d Ft" % (nap[i],fuvar[i],kmtoft(hossz[i])))
