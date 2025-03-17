#include <iostream>

using namespace std;

int main(){
    int hazszam[32] = {5,21,2,18,7,9,15,23,25,8,10,16,24,26,32,1,3,13,19,29,31,6,12,22,28,17,4,20,11,27,14,30};
    int i,j,csere;
    for(i=0;i<=31;i++)
        cout << hazszam[i] << ' ';
    cout << endl;
    for(i=0;i<=30;i++)
        for(j=31;j>i;j--)
        if (hazszam[j-1]>hazszam[j]){
                csere = hazszam[j];
                hazszam[j]=hazszam[j-1];
                hazszam[j-1]=csere;
        }
    for(i=0;i<=31;i++)
        cout << hazszam[i] << ' ';
}
