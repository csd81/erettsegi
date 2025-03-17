#include <iostream>

using namespace std;

int kerekit(int be){
    int ki;
    ki = 100*(be / 100);
    if (be % 100 >=50) ki+=100;
    return ki;
}

int kedvezmeny(int a, int h, int sz){
    if (h<=25 || sz<=15) a*=0.8;
    return a;
}

int ado(int hosszusag, int szelesseg){
    int fab, terulet;
    terulet=hosszusag*szelesseg;
    fab=terulet*51;
    if (terulet>700) fab+=39*300;
    if (terulet>1000) fab+=200;
    return fab;
}

int main(){
    cout << kerekit(6238) << endl;
    cout << kerekit(6586) << endl;
    cout << kedvezmeny(1000,15,15) << endl;
    cout << kedvezmeny(1000,35,15) << endl;
    cout << kedvezmeny(1000,35,10) << endl;
    cout << kedvezmeny(1000,35,25) << endl;
    cout << ado(50,30) << endl;
    cout << ado(20,40) << endl;
    cout << ado(20,25) << endl;
}
