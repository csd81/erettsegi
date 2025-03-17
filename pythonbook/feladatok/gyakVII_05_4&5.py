class Tortek:
    def __init__(self):
        self.szamlalo = 0
        self.nevezo = 1

    def kiir(self):
        print("%d/%d" % (self.szamlalo,\
            self.nevezo),end=" ")
        
    def beker(self):
        self.szamlalo = int(input("Kérem a számlálót: "))
        self.nevezo = int(input("Kérem a nevezőt: "))        

    def szamlalotad(self):
        return self.szamlalo

    def nevezotad(self):
        return self.nevezo

    def lnko(a,b):
        if a == b:
            return a
        if a < b:
            return Tortek.lnko(a, b - a)
        if a > b:
            return Tortek.lnko(a - b, b)
        
    def egyszerusit(self):
        if self.szamlalo % self.nevezo == 0:
            print("= %d" % (self.szamlalo / self.nevezo))
        else:
            print("= %d/%d" %  \
            (self.szamlalo/Tortek.lnko(self.szamlalo,self.nevezo), \
            self.nevezo/Tortek.lnko(self.szamlalo,self.nevezo)))

    def egesz_e(self):
        if self.szamlalo % self.nevezo == 0:
            print(int(self.szamlalo / self.nevezo))
        else:
            print("Nem egész!")

    def megad(self, sz, n):
        self.szamlalo, self.nevezo = sz,n

class Muveletek:
    def __init__(self):
        self.tort1 = Tortek()
        self.tort2 = Tortek()
        self.eredmeny = Tortek()
        self.muvjel = "*"
        
    def kiir(self):
        self.tort1.kiir()
        print("%s " % \
         (self.muvjel), end ='')
        self.tort2.kiir()
        print("= ", end = '')

    def beker(self):
        print("1. tört")
        self.tort1.beker()
        print("2. tört")
        self.tort2.beker()

    def szoroz(self):
        self.sz = self.tort1.szamlalotad() \
                  * self.tort2.szamlalotad()
        self.n = self.tort1.nevezotad()\
                 * self.tort2.nevezotad()
        self.eredmeny.megad(self.sz,self.n)
        self.kiir()
        self.eredmeny.kiir()
        self.eredmeny.egyszerusit()

    def lkkt(a,b):
        return int(a * b / Tortek.lnko(a,b))
        
    def osszead(self):
        self.kn = Muveletek.lkkt(self.tort1.nevezotad(),self.tort2.nevezotad())
        self.sz1 = self.tort1.szamlalotad() * self.kn / self.tort1.nevezotad()
        self.sz2 = self.tort2.szamlalotad() * self.kn / self.tort2.nevezotad()
        self.eredmeny.megad(self.sz1 + self.sz2, self.kn)
        self.kiir()
        self.tort1.megad(self.sz1,self.kn)
        self.tort2.megad(self.sz2,self.kn)
        self.kiir()
        self.eredmeny.kiir()
        self.eredmeny.egyszerusit()
        
    def valaszt(self):
        if self.muvjel == "*":
            self.szoroz()
        elif self.muvjel == ":":
            self.oszt()
        elif self.muvjel == "-":
            self.kivon()
        else:
            self.osszead()

    def megad(self, sz1, n1, sz2, n2, muv):
        self.tort1.megad(sz1,n1)
        self.tort2.megad(sz2,n2)
        self.muvjel = muv
        
    def oszt(self):
        self.sz = self.tort1.szamlalotad() \
                  * self.tort2.nevezotad()
        self.n = self.tort1.nevezotad()\
                 * self.tort2.szamlalotad()
        self.eredmeny.megad(self.sz,self.n)
        self.kiir()
        self.muvjel = '*'
        self.sz = self.tort2.nevezotad()
        self.n = self.tort2.szamlalotad()
        self.tort2.megad(self.sz,self.n)
        self.kiir()
        self.eredmeny.kiir()
        self.eredmeny.egyszerusit()
        
    def kivon(self):
        self.kn = Muveletek.lkkt(self.tort1.nevezotad(),self.tort2.nevezotad())
        self.sz1 = self.tort1.szamlalotad() * self.kn / self.tort1.nevezotad()
        self.sz2 = self.tort2.szamlalotad() * self.kn / self.tort2.nevezotad()
        self.eredmeny.megad(self.sz1 - self.sz2, self.kn)
        self.kiir()
        self.tort1.megad(self.sz1,self.kn)
        self.tort2.megad(self.sz2,self.kn)
        self.kiir()
        self.eredmeny.kiir()
        self.eredmeny.egyszerusit()

    def muveletetmegad(self, jel):
        self.muvjel = jel
            
muvelet = Muveletek()
muvelet.beker()
muvelet.valaszt()
muvelet.muveletetmegad('+')
muvelet.valaszt()


