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
    cout << lnko(6,6) << endl;
    cout << lnko(120,75) << endl;
    cout << lnko(75,120) << endl;
    cout << lkkt(75,120) << endl;
    egyszerusit(12,15);
    egyszerusit(6,2);
    szoroz(2,3,3,4);
    osszead(1,2,3,4);
}
