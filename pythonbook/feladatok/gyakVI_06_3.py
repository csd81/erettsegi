word = input("Kérek egy kódsorozatot: ")
corr = "BJEH"
n = len(word)
i = 0    
while i < n and corr.find(word[i]) > -1:
    i += 1
if i >= n:
    print("Jó kódsor.")
else:
    print("Hibás kódsor")

