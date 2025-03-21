#include <iostream>

using namespace std;

int main(){
    int hazszam[32] = {5,21,2,18,7,9,15,23,25,8,10,16,24,26,32,1,3,13,19,29,31,6,12,22,28,17,4,20,11,27,14,30};
    int szelesseg[32] = {15,15,15,15,20,20,20,20,20,20,15,20,20,20,20,25,25,25,25,25,25,25,30,25,25,30,30,30,35,35,35,35};
    int hosszusag[32] = {55,50,0,0,45,40,30,45,35,0,0,0,0,0,0,25,45,35,45,40,30,0,0,0,0,25,0,0,30,35,0,0};
    int i,t,minterulet,maxterulet,minhely,maxhely;
    minhely=-1;
    maxhely=-1;
    minterulet=10000; //+v�gtelen
    maxterulet=0; //-v�gtelen
    for(i=0;i<=31;i++){
        t = hosszusag[i]*szelesseg[i];
        if (t<minterulet && hazszam[i]%2 == 1){
            minterulet=t;
            minhely=hazszam[i];
        }
        if (t>maxterulet && hazszam[i]%2 ==1){
            maxterulet=t;
            maxhely=hazszam[i];
        }
    }
    cout << "Legkisebb telek hazszam: " << minhely
         << ", meret negyzetmeterben: " << minterulet << endl;
    cout << "Legnagyobb telek hazszam: " << maxhely
         << ", meret negyzetmeterben: " << maxterulet << endl;
    cout << "Telkek szama kozottuk: " << (maxhely-minhely)/2 -1;
}
