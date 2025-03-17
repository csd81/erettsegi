#include <iostream>
#include <map>

using namespace std;

int main(){
    //a - b) feladat
    int tabla[8][8] = {
        {0,0,0,0,0,4,0,12},
        {0,0,5,0,0,0,0,0},
        {0,0,0,0,0,0,0,6},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0},
        {0,0,0,0,0,0,0,0}
    };
    //c) feladat
    cout << "2. sor 3 oszlop: "<< tabla[1][2] << endl;
    //d) feladat
    int s,o;
    cout << "Kerek egy sor es egy oszlop szamot 1 1 alakban (1..8): ";
    cin >> s >> o;
    cout << tabla[s-1][o-1] << endl;
    //e) feladat
    char fig[13] ={'.','G','H','F','B','V','K','g','h','f','b','v','k'};
    cout << fig[tabla[s-1][o-1]] << endl << endl;
    //f) feladat
    string poz;
    cout << "Kerek egy poziciot (pl. A5): ";
    cin >> poz;
    map <char, int> bsz;
    bsz['A']=0;
    bsz['B']=1;
    bsz['C']=2;
    bsz['D']=3;
    bsz['E']=4;
    bsz['F']=5;
    bsz['G']=6;
    bsz['H']=7;
    bsz['1']=0;
    bsz['2']=1;
    bsz['3']=2;
    bsz['4']=3;
    bsz['5']=4;
    bsz['6']=5;
    bsz['7']=6;
    bsz['8']=7;
    cout << endl << fig[tabla[bsz[poz[0]]][bsz[poz[1]]-1]];
}
