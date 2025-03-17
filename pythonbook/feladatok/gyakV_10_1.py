dn = ["hétfő", "kedd", "szerda",
     "csütörtök", "péntek",
      "szombat", "vasárnap"]
re = open("tavok.txt",'r')
line = re.readline()
while line != "":
    line = line.strip()
    datas = line.split()
    d = int(datas[0])
    print("%s %s. fuvar: %s km" % (dn[d-1], datas[1], datas[2]))
    line = re.readline()
re.close()
