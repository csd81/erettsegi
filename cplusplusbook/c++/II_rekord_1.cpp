#include <iostream>

using namespace std;

int main(){
    //a) feladat
    struct telek {
        int hazszam;
        int szeles;
        int hossz;
    };
    //b) feladat
    telek buff;
    //c) feladat
    telek telkek[50];
    //d) feladat
    buff.hazszam = 21;
    buff.szeles = 15;
    buff.hossz = 50;
    //e) feladat
    telkek[10] = buff;
    //f) feladat
    cout << "A " << buff.hazszam << ". szamu telek terulete "
        << buff.szeles*buff.hossz <<" negyzetmeter" << endl;
    //g) feladat
    buff.szeles+=10;
    buff.hossz-=10;
}
