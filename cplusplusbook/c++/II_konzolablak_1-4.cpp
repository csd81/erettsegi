#include <iostream>

using namespace std;

int main(){
    //1. feladat
    string nev;
    cout << "Mi a neved? ";
    cin >> nev;
    cout << "Hello " << nev << endl << endl;
    //2. feladat
    int egesz;
    cout << "Kerek egy egesz szamot: ";
    cin >> egesz;
    cout << "A 2. feladat tesztje: " << egesz << '.' << endl << endl;
    //3. feladat
    string szo1="abba";
    string szo2="baba";
    cout << "A " << szo2 << " az " << szo1 << " anagrammaja." << endl << endl;
    //4. feladat
    int sz1 = 24;
    int n1 = 32;
    int sz2 = 3;
    int n2 = 4;
    cout << sz1 << '/' << n1 << " = " << sz2 << '/' << n2;

}
