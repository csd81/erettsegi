import sys

def mt():
    for i in range(1,16):
        for j in range(1,16):
            print("%d " % (i * j),  end = '')
        print()

mt()
oldout = sys.stdout
wr = open("multitable.txt",'w')
sys.stdout = wr
mt()
wr.close()
sys.stdout = oldout
print("Kész a fájl.")
