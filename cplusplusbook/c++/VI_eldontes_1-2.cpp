#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    //1. feladat
    srand(time(NULL));
    int tomb[10];
    int i;
    for(i=0;i<=9;i++){
        tomb[i] = rand()%6+1;
        cout << tomb[i] << ' ';
    }
    i=0;
    while (i<=9 && tomb[i]!=6)
        i++;
    if (i>9) cout << "Nincs koztuk 6-os.";
    else cout << "Van koztuk 6-os.";
    //2. feladat
    string szo;
    cout << endl << "Kerek egy szot: ";
    cin >> szo;
    string mgh="aeiou";
    i=0;
    while (i<=szo.length()-1 && mgh.find(szo[i])==string::npos)
        i++;
    if (i>szo.length()-1) cout << "Nincs benne maganhangzo.";
    else cout << "Van benne maganhangzo.";

}
