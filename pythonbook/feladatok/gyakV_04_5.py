st = input("Kérek egy szöveget 4/11 akármi formában: ")
words = st.split()
wolves = words[0].split('/')
n1, n2 = int(wolves[0]), int(wolves[1])
print("A farkasok száma: ", n1 + n2)



