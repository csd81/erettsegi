#include <iostream>

using namespace std;
int lnko(int a, int b){
    if (a==b) return a;
    if (a<b) return lnko(a,b-a);
    if (a>b) return lnko(a-b,b);
}
int lkkt(int a, int b){
    return a*b/lnko(a,b);
}

void egyszerusit(int szaml, int nev){
    cout << " = ";
    if (szaml % nev == 0) cout << szaml/nev;
    else cout << szaml/lnko(szaml,nev) << '/' << nev/lnko(szaml,nev);
    cout << endl;
}
void szoroz(int szaml1, int nev1, int szaml2, int nev2){
    cout << szaml1 << '/' << nev1 << " * " << szaml2 << '/'
         << nev2 << " = " << szaml1*szaml2 << '/' << nev1*nev2;
    egyszerusit(szaml1*szaml2,nev1*nev2);
}
void osszead(int szaml1, int nev1, int szaml2, int nev2){
    int kn, bov1, bov2;
    kn = lkkt(nev1,nev2);
    bov1 = szaml1*kn/nev1;
    bov2 = szaml2*kn/nev2;
    cout << szaml1 << '/' << nev1 << " + " << szaml2 << '/' << nev2
         << " = " << bov1 << '/' << kn << " + " << bov2 << '/' << kn
         << " = " << bov1+bov2 << '/' << kn;
    egyszerusit(bov1+bov2,kn);
}

int main(){
    int sz1,n1,sz2,n2;
    cout << "Kerem az 1. tort szamlalojat es nevezojet 12 15 alakban: ";
    cin >> sz1 >> n1;
    cout << "Kerem a 2. tort szamlalojat es nevezojet 12 15 alakban: ";
    cin >> sz2 >> n2;
    cout << sz1 << '/' << n1;
    egyszerusit(sz1,n1);
    cout << sz2 << '/' << n2;
    egyszerusit(sz2,n2);
    szoroz(sz1,n1,sz2,n2);
    osszead(sz1,n1,sz2,n2);
}
