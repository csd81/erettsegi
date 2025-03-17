#include <iostream>
#include <fstream>




using namespace std;


class Tortek {
    private:
        int szamlalo;
        int nevezo;
    public:
        Tortek (){
            szamlalo=0;
            nevezo=1;
        }
        void eldontiegesze(){
            if (szamlalo%nevezo==0)
                cout << szamlalo/nevezo;
            else
                cout << "Nem egesz";
            cout << endl;
        }
        static int lnko(int egyik, int masik){
            if (egyik==masik)
                return egyik;
            if (egyik<masik)
                return lnko(egyik,masik-egyik);
            if (egyik>masik)
                return lnko(egyik-masik,masik);
        }
        void egyszerusit(){
            cout <<" = ";
            if (szamlalo%nevezo==0)
                cout << szamlalo/nevezo;
            else
                cout
                    << szamlalo/
                    lnko(szamlalo,nevezo)
                    << "/"
                    << nevezo/
                    lnko(szamlalo,nevezo);
            cout << endl;
        }
        void megjelenit(){
            cout << szamlalo
                << "/" << nevezo;
        }
        void tortetbeker(){
            cout <<
             "Kerem a szamokat 12 15 alakban: ";
            cin >> szamlalo >> nevezo;
        }
        int szamlalotad(){
            return szamlalo;
        }
        int nevezotad(){
            return nevezo;
        }
        void tortetfeltolt(int sz, int n){
            szamlalo = sz;
            nevezo = n;
        }
};
class Muveletek {
    protected:
        Tortek tort1;
        Tortek tort2;
        Tortek eredmeny;
        char muvelet;
    public:
        Muveletek(){
            muvelet = '*';
        }
        virtual void eredmenytkiir(){};
        virtual void muveletetvegez(){};
        void muveletetbeker(){
            cout << "1. tort" << endl;
            tort1.tortetbeker();
            cout << "2. tort" << endl;
            tort2.tortetbeker();
        }
        void adatotfeltolt(int sz1,
                int n1, int sz2,
                int n2, char m){
            tort1.tortetfeltolt(sz1,n1);
            tort2.tortetfeltolt(sz2,n2);
            muvelet = m;
        }
        void fajlbair(){
            streambuf *eredeti
                = cout.rdbuf();
            ofstream ki(
                "d:\\eredmeny.txt",ios::app);
            cout.rdbuf(ki.rdbuf());
            eredmenytkiir();
            ki.flush();
            ki.close();
            cout.rdbuf(eredeti);
        }
};
class Osszeadasok
        : public Muveletek {
    private:
        Tortek resz1;
        Tortek resz2;
    public:
        Osszeadasok(){
            muvelet = '+';
        }
    public:
        void eredmenytkiir(){
            tort1.megjelenit();
            cout <<" " << muvelet << " ";
            tort2.megjelenit();
            cout <<" = ";
            resz1.megjelenit();
            cout <<" " << muvelet << " ";
            resz2.megjelenit();
            cout <<" = ";
            eredmeny.megjelenit();
            eredmeny.egyszerusit();
        }
        int lkkt(int a, int b){
            return a*b/Tortek::lnko(a,b);
        }
        void muveletetvegez(){
            int knev = lkkt(
                tort1.nevezotad(),
                tort2.nevezotad());
            int sz1 =
                tort1.szamlalotad()*
                knev/tort1.nevezotad();
            int sz2 =
                tort2.szamlalotad()*
                knev/tort2.nevezotad();
            resz1.tortetfeltolt(sz1,knev);
            resz2.tortetfeltolt(sz2,knev);
            eredmeny.tortetfeltolt(
                            sz1+sz2,knev);
        }
};
class Szorzasok
    : public Muveletek {
    public:
        void muveletetvegez(){
            eredmeny.tortetfeltolt(
                tort1.szamlalotad()*
                tort2.szamlalotad(),
                tort1.nevezotad()*
                tort2.nevezotad());
        }
        void eredmenytkiir(){
            tort1.megjelenit();
            cout <<" " << muvelet << " ";
            tort2.megjelenit();
            cout <<" = ";
            eredmeny.megjelenit();
            eredmeny.egyszerusit();
        }
};
class Control {
    private:
        Tortek tort;
        Szorzasok szorzas;
        Osszeadasok osszeadas;
    public:
        Control(){
            tort.tortetbeker();
            tort.eldontiegesze();
            tort.megjelenit();
            tort.egyszerusit();
            szorzas.muveletetbeker();
            szorzas.muveletetvegez();
            szorzas.eredmenytkiir();
            osszeadas.muveletetbeker();
            osszeadas.muveletetvegez();
            osszeadas.eredmenytkiir();
            int sz1,n1,sz2,n2;
            char m;
            fstream be("adat.txt",ios::in);
            be >> sz1 >> n1 >> sz2 >> n2 >> m;
            while (!be.eof()){
                if (m='*'){
                    szorzas.adatotfeltolt(
                        sz1,n1,sz2,n2,m);
                    szorzas.muveletetvegez();
                    szorzas.fajlbair();
                }
                else {
                    osszeadas.adatotfeltolt(
                        sz1,n1,sz2,n2,m);
                    osszeadas.muveletetvegez();
                    osszeadas.fajlbair();
                }
                be >> sz1 >> n1 >> sz2 >> n2 >> m;
            }
            be.close();
        }
};
int main(){
    Control control;
}
