#include <iostream>

using namespace std;

int main(){
    int oszto,vizsgalt;
    cout << "Kerem a vizsgalt szamot: ";
    cin >> vizsgalt;
    cout << endl << vizsgalt << "=";
    oszto=2;
    while (!(vizsgalt / oszto == 1 && vizsgalt % oszto == 0)){
        if (vizsgalt % oszto ==0) {
            vizsgalt=vizsgalt /oszto;
            cout << oszto <<"*";
        }
        else oszto++;
    }
    cout << oszto <<"*1";
}
