def cont(v):
    db = 0
    for i in range(len(v)):
        if c[i] == v[i]:
            db += 1
    return db

c = "BAACAABBCCCBABB"
t = input("Kérem a vizsgázó válaszait: ")
print("A helyes megoldások száma: ", cont(t))
