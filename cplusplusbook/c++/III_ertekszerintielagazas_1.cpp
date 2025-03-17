#include <iostream>

using namespace std;

int main(){
    //1. feladat
    int szam, t, e;
    cout << "Kerek egy egesz szamot 0-255: ";
    cin >> szam;
    char ki;
    t = szam / 16;
    e = szam % 16;
    switch (t){
        case 10: ki='A'; break;
        case 11: ki='B'; break;
        case 12: ki='C'; break;
        case 13: ki='D'; break;
        case 14: ki='E'; break;
        case 15: ki='F'; break;
        default:
            ki = (char)(t+48);
    }
    cout << ki ;
    switch (e){
        case 10: ki='A'; break;
        case 11: ki='B'; break;
        case 12: ki='C'; break;
        case 13: ki='D'; break;
        case 14: ki='E'; break;
        case 15: ki='F'; break;
        default:
            ki = (char)(e+48);
    }
    cout << ki ;
}
