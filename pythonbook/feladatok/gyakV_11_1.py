re = open("adat.txt",'r')
wr = open("oper.txt",'w')
line = re.readline()
while line !="":
    line = line.strip()
    datas = line.split()
    wr.write("%s/%s %s %s/%s =\n" % \
          (datas[0], datas[1],
           datas[4], datas[2],
           datas[3]))
    line = re.readline()
re.close()
wr.close()
