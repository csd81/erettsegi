word = input("Kérek egy szót: ")
vowels = "aeiou"
n = len(word)
i = 0    
while i < n and vowels.find(word[i]) > -1:
    i += 1
if i >= n:
    print("Nincs benne magánhangzó.")
else:
    print("Van benne magánhangzó")

