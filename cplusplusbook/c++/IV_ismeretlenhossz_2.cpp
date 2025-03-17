#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int nap, fuvar, hossz;
    string napok[7]= {"hetfo","kedd","szerda","csutortok",
                      "pentek","szombat","vasarnap"};
    fstream be("tavok.txt",ios::in);
    be >> nap >> fuvar >> hossz;
    while (!be.eof()){
        cout << napok[nap-1] << ' ' << fuvar <<". fuvar: " << hossz
             << " km" << endl;
        be >> nap >> fuvar >> hossz;
    }
    be.close();
}
