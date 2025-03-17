#tipp = [8, 1, 2, 1, 4, 4, 2, 4, 9]
tipp = [3, 3, 1, 1, 4, 3, 1, 3, 4]
#tipp = [6, 3, 4, 3, 3, 6, 2, 3, 2]
rend = tipp.copy()
rend.sort()
n = len(rend)
nytipp = 0
i = 0
while i < n - 1 and rend[i] == rend[i + 1]:
    j = i + 2
    while j < n - 1 and rend[j] == rend[i]:
        j += 1
    i = j
if i < n - 1:
    nytipp = rend[i]
else:
    if rend[n - 1] == rend[n - 2]:
        print("Nem volt egyedi tipp a megadott fordulóban!")
    else:
        nytipp = rend[n - 1]
if nytipp > 0:
    print("A nyertes tipp: %d, aki tippelte %d." % (nytipp, 1 + tipp.index(nytipp)))
