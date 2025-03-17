#include <iostream>
#include <cmath>

using namespace std;

int main(){
    //1. feladat
    float v;
    cout << "Kerek egy valos szamot: ";
    cin >> v;
    if (v<0) v = -1*v;
    cout << "A szam abszoluterteke: " << v << endl;
    //2. feladat
    cout << "Kerek egy valos szamot: ";
    cin >> v;
    if (v<0)
        cout << "Negativ szambol nem lehet gyokot vonni." << endl;
    else
        cout << "A szam negyzetgyoke : " << sqrt(v) << endl;
    //3. feladat
    int hsz;
    cout << "Kerem a tornybol lathato hajok szamat: " ;
    cin >> hsz;
    if (hsz > 3) cout << "Nehez torony." << endl;
    //4. feladat
    int sz, n;
    cout << "Kerek ket egesz szamot 12 15 alakban: ";
    cin >> sz >> n;
    if (sz % n == 0)
        cout << "Erteke: " << sz/n << '.' << endl;
    else
        cout << "Nem egesz."  << endl;
    //5. feladat
    int am,t,e;
    cout << "Kerek egy haromjegyu egesz szamot: ";
    cin >> am;
    sz = am/100;
    t = am/10 % 10;
    e = am % 10;
    if (am == sz*sz*sz+t*t*t+e*e*e)
        cout << "Amstrong-szam." << endl;
    else
        cout << "Nem Amstrong-szam"  << endl;
}
