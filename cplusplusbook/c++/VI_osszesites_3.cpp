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
    return kerekit(kedvezmeny(fab,hosszusag,szelesseg));
}

int main(){
    int hazszam[32] = {5,21,2,18,7,9,15,23,25,8,10,16,24,26,32,1,3,13,19,29,31,6,12,22,28,17,4,20,11,27,14,30};
    int szelesseg[32] = {15,15,15,15,20,20,20,20,20,20,15,20,20,20,20,25,25,25,25,25,25,25,30,25,25,30,30,30,35,35,35,35};
    int hosszusag[32] = {55,50,0,0,45,40,30,45,35,0,0,0,0,0,0,25,45,35,45,40,30,0,0,0,0,25,0,0,30,35,0,0};
    int ossz=0;
    for(int i=0;i<=31;i++)
        if (hazszam[i]%2==1)
            ossz+=ado(hosszusag[i],szelesseg[i]);
    cout << "Gazdagsor adoja Fabatkaban: " << ossz;

}
