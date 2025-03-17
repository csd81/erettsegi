from random import randrange
signs = ["+","-","*",":"]
wr = open("fracts.txt",'w')
for i in range(100):
    datas = []
    for j in range(4):
        datas.append(randrange(1,100))
    datas.append(signs[randrange(0,4)])
    wr.write("%d/%d %s %d/%d =\n" % \
          (datas[0], datas[1],
           datas[4], datas[2],
           datas[3]))
wr.close()
