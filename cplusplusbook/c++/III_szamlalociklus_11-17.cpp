#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    //11. feladat
    int i;
    string napok[7] = {"hetfo","kedd","szerda","csutortok",
                        "pentek","szombat","vasarnap"};
    for(i=0;i<=6;i++)
        cout << napok[i] << ' ';
    //12. feladat
    cout << endl;
    srand(time(NULL));
    int vel;
    for(i=1;i<=15;i++){
        vel = rand()%7;
        cout << napok[vel] << ' ';
    }
    cout << endl;
    //13. feladat
    char fig[3] = {'X','O','.'};
    for(i=0;i<=2;i++)
        cout << fig[i];
    //14. feladat
    cout << endl;
    bool dobas[100];
    for(i=0;i<=99;i++)
        dobas[i]=rand()%2;
    for(i=0;i<=99;i++){
        if (dobas[i]==true) cout << "fej" << ' ';
        else cout << "iras" << ' ';
    }
    //15. feladat
    cout << endl;
    int kocka[50];
    for(i=0;i<=49;i++)
        kocka[i]=rand()%6+1;
    for(i=0;i<=49;i++)
        cout << kocka[i] << ' ';
    //16. feladat
    string szo, seged;
    cout << endl << "Kerek egy szot: ";
    cin >> szo;
    seged="";
    for(i=szo.length()-1;i>=0;i--)
        seged+=szo[i];
    szo=seged;
    cout << szo;
    //17. feladat
    string bazissor;
    char bazisok[4] = {'A','C','G','T'};
    bazissor="";
    for(i=0;i<=19;i++)
        bazissor+=bazisok[rand()%4];
    cout << endl << bazissor;

}
