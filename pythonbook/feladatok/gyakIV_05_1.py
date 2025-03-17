ch = input("Kérek egy karaktert: ")
#első megoldás
if '0' <= ch and ch <= '9':
    print("Számjegy")
else:
    print("Nem számjegy")
#második megoldás
if 48 <= ord(ch) and ord(ch) <= 57:
    print("Számjegy")
else:
    print("Nem számjegy")
