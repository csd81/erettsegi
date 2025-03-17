#include <iostream>

using namespace std;

int main(){
    //a) feladat
    struct igenyek {
        int ora;
        int perc;
        int masodperc;
        int csapat;
        int indul;
        int erkezik;
    };
    //b) feladat
    igenyek igeny[120];
    //c) feladat
    igenyek buff;
    //d) feladat
    igeny[0].ora = 10;
    igeny[0].perc = 15;
    igeny[0].masodperc = 0;
    igeny[0].csapat = 4;
    igeny[0].indul = 2;
    igeny[0].erkezik = 10;
    igeny[10].ora = 20;
    igeny[10].perc = 10;
    igeny[10].masodperc = 0;
    igeny[10].csapat = 4;
    igeny[10].indul = 4;
    igeny[10].erkezik = 7;
    //e) feladat
    igeny[0].ora++;
    igeny[10].ora--;
    //f) feladat
    buff = igeny[0];
    igeny[0] = igeny[10];
    igeny[10] = buff;
    //g) feladat
    cout << igeny[0].ora << ':' << igeny[0].perc << ':'
         << igeny[0].masodperc << ' ' << igeny[0].csapat
         << ' ' << igeny[0].indul << ' ' << igeny[0].erkezik << endl;
    cout << igeny[10].ora << ':' << igeny[10].perc << ':'
         << igeny[10].masodperc << ' ' << igeny[10].csapat
         << ' ' << igeny[10].indul << ' ' << igeny[10].erkezik << endl;

}
