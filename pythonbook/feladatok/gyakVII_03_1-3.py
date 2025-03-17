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
            print("= %d" % (int(self.szamlalo / self.nevezo)))
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
        
tort = Tortek()
tort.beker()
tort.egesz_e()
tort.kiir()
tort.egyszerusit()


