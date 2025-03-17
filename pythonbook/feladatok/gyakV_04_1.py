word = input("Kérek egy szót: ")
vowels = "aeiouAEIOU"
#1. feladat
if vowels.find(word[0]) > -1:
    print("Magánhangzóval kezdődik.")
else:
    print("Nem magánhangzóval kezdődik.")
#2. feladat
word = word.lower()
if word.find('e') > -1:
    print("Van benne e/E.")
else:
    print("Nincs benne e/E.")
