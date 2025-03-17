#include <iostream>

using namespace std;

int main(){
    //a - b) feladatok
    string napok[7] = {"hetfo","kedd","szerda","csutortok",
                        "pentek", "szombat", "vasarnap"};
    //c) feladat
    cout << napok[0] << endl;
    //d) feladat
    cout << napok[2] << endl;
    //e) feladat
    cout << napok[5];
    cout << endl << "A het hanyadik napjat irjuk ki? (1-7) ";
    int napszam;
    cin >> napszam;
    cout << napok[napszam-1];
}
