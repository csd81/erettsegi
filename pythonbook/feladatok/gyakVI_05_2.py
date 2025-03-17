nap = [3,1,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,5]
fuvar = [3,1,7,2,3,4,5,6,8,9,10,11,1,2,4,5,6,7,8,9,10,11,12,13,14,15,4,1,2,3,5,6,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,17,18,19,1,2,8,3,4,5,6,7,20]
hossz = [10,3,14,3,1,9,5,2,9,8,5,6,7,7,2,4,6,3,5,8,1,4,2,3,5,2,28,11,2,3,7,11,2,5,2,6,2,3,2,6,2,2,4,2,2,4,4,5,2,7,2,3,5,12,25,6,6,6,9,6,7]

#a) feladat
minnap = 10
maxnap = 0
for i in range(len(nap)):
    if nap[i] < minnap:
        minnap = nap[i]
    if nap[i] > maxnap:
        maxnap = nap[i]
print("A(z) %d. napon dolgozott először a héten a futár." % (minnap))    

#b) feladat
minfuv, kme, maxfuv, kmu = 1000, 0, 0, 0
for i in range(len(nap)):
    if nap[i] == minnap and minfuv > fuvar[i]:
        minfuv = fuvar[i]
        kme = hossz[i]
    if nap[i] == maxnap and maxfuv < fuvar[i]:
        maxfuv = fuvar[i]
        kmu = hossz[i]
print("A hét első útja: %d km" % (kme))

#c) feladat
print("A hét utolsó útja: %d km" % (kmu))

#d) feladat
db = [0]*8
for i in range(len(nap)):
    db[nap[i]] += 1

maxhely = 0
maxertek = 0
for i in range(8):
    if db[i] > maxertek:
        maxhely = i
        maxertek = db[i]
print("A hét %d. napján volt a legtöbb fuvar." % (maxhely))
