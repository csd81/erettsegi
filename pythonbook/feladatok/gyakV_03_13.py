word = input("Kérek egy szót: ")
n = len(word)
#a) feladat
for i in range(n-1,-1,-1):
    print(word[i], sep="", end="")
print("\n")
#b) feladat
b = ""
for i in range(n-1,-1,-1):
    b += word[i]
word = b
print(word)
#c) feladat
for i in range(n-1,-1,-1):
    word = word + word[i]
word = word[:n]
print(word)
