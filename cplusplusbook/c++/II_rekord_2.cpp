#include <iostream>

using namespace std;

int main(){
    //a) feladat
    struct tmuv {
        int sz1;
        int n1;
        int sz2;
        int n2;
        char jel;
    };
    //b) feladat
    tmuv atm;
    //c) feladat
    tmuv tmuvel[100];
    //d) feladat
    tmuvel[0].sz1 = 8;
    tmuvel[0].n1 = 20;
    tmuvel[0].sz2 = 8;
    tmuvel[0].n2 = 30;
    tmuvel[0].jel ='*';
    //e) feladat
    atm = tmuvel[0];
    //f) feladat
    cout << tmuvel[0].sz1 << '/' << tmuvel[0].n1 << " * ";
    cout << tmuvel[0].sz2 << '/' << tmuvel[0].n2 << " = ";
    cout << tmuvel[0].sz1 * tmuvel[0].sz2 << '/'
         << tmuvel[0].n1 * tmuvel[0].n2;

}
