#include <iostream>

using namespace std;

int main(){
    int nap[60]={3,1,1,1,1,1,1,1,1,1,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,5};
    int fuvar[60]={3,1,2,3,4,5,6,8,9,10,11,1,2,4,5,6,7,8,9,10,11,12,13,14,15,4,1,2,3,5,6,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,17,18,19,1,2,8,3,4,5,6,7,20};
    int hossz[60]={10,3,3,1,9,5,2,9,8,5,6,7,7,2,4,6,3,5,8,1,4,2,3,5,2,28,11,2,3,7,11,2,5,2,6,2,3,2,6,2,2,4,2,2,4,4,5,2,7,2,3,5,12,25,6,6,6,9,6,7};
    //a) feladat
    string hetnapjai[7]={"hetfo","kedd","szerda","csutortok","pentek",
                    "szombat","vasarnap"};
    int i,minnap,minfuvar,minhely;
    minnap=nap[0];
    for(i=1;i<=59;i++)
        if (nap[i]<minnap)
            minnap=nap[i];
    cout << "Elso nap, mikor dolgozott a heten: " << hetnapjai[minnap-1] << endl;
    //b) feladat
    minfuvar=10000; //+v�gtelen
    minhely=-1;
    for(i=0;i<=59;i++)
        if (fuvar[i]<minfuvar && nap[i] == minnap){
            minhely = i;
            minfuvar = fuvar[i];
        }
    cout << "A het elso fuvarjanak adatai: " << endl;
    cout << hetnapjai[nap[minhely]-1] << ' ' << fuvar[minhely] << ". fuvar: "
         << hossz[minhely] << " km" << endl;
    //c) feladat
    int maxnap, maxfuvar, maxhely;
    maxnap=nap[0];
    for(i=1;i<=59;i++)
        if (nap[i]>maxnap)
            maxnap=nap[i];
    maxfuvar=0; //-v�gtelen
    maxhely=-1;
    for(i=0;i<=59;i++)
        if (fuvar[i]>maxfuvar && nap[i] == maxnap){
            maxhely = i;
            maxfuvar = fuvar[i];
        }
    cout << "A het utolso fuvarjanak adatai: " << endl;
    cout << hetnapjai[nap[maxhely]-1] << ' ' << fuvar[maxhely] << ". fuvar: "
         << hossz[maxhely] << " km" << endl;
    //d) feladat
    int db[8];
    for(i=1;i<=7;i++)
        db[i]=0;
    for(i=0;i<=59;i++)
        db[nap[i]]++;
    maxhely=1;
    maxnap=db[1];
    for(i=2;i<=7;i++)
        if (maxnap<db[i]){
            maxnap=db[i];
            maxhely=i;
        }
    cout << "Legtobb fuvar: " << hetnapjai[maxhely-1] ;
}
