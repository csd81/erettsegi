def test(v):
    dbv = 0
    db = len(v)
    vowels="aeiou"
    for i in range(db):
        if vowels.find(v[i]) > -1:
            dbv += 1
    return dbv > db - dbv

dbw = 0
dbt = 0
inp = open("szoveg.txt",'r')
line = inp.readline()
while line != "":
    dbw += 1
    line = line.strip()
    if test(line):
        dbt += 1
        print(line, end=' ')
    line = inp.readline()

print("\n%d/%d : %.2f" % (dbt, dbw, 100*dbt/dbw), end='')
print('%')
