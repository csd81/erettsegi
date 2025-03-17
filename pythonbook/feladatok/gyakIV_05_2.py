ch = input("Kérek egy karaktert: ")
#első megoldás
if 'A' <= ch and ch <= 'Z' or 'a' <= ch and ch <= 'z':
    print("Betű")
else:
    print("Nem betű")
#második megoldás
if 65 <= ord(ch) and ord(ch) <= 90 or 97 <= ord(ch) and ord(ch) <= 122:
    print("Betű")
else:
    print("Nem betű")
