#include <iostream>
#include <fstream>

using namespace std;

int main(){
    //1. feladat
    int r, g, b;
    fstream be("kep.txt",ios::in);
    be >> r >> g >> b;
    be.close();
    cout << "piros: " << r <<", zold: " << g <<", kek: " << b << endl;

    //2. feladat
    int sz1, n1, sz2, n2;
    char muv;
    fstream betolt("adat.txt",ios::in);
    betolt >> sz1 >> n1 >> sz2 >> n2 >> muv;
    betolt.close();
    cout << sz1 << '/' << n1 << ' ' << muv << ' ' << sz2
        << '/' << n2 << " = " << endl;

    //3. feladat
    int nap, fuvar, tav;
    string napok[7]= {"hetfo","kedd","szerda","csutortok",
                      "pentek","szombat","vasarnap"};
    fstream befele("tavok.txt",ios::in);
    befele >> nap >> fuvar >> tav;
    befele.close();
    cout << napok[nap] <<' ' << fuvar <<". fuvar: " << tav << " km" << endl;
}
