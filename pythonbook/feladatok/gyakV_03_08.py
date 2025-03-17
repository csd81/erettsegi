ln = input("Kérem a vezetéknevet: ")
fn = input("Kérem a keresztnevet: ")
name = ln[:3] + fn[:3] + "01"
name = name.lower()
print(name)
