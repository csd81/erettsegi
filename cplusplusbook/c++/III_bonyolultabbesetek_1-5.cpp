#include <iostream>
#include <cmath>

using namespace std;

int main(){
    //1. feladat
    float v;
    cout << "Kerek egy valos szamot: ";
    cin >> v;
    if (v<0) cout << "A szam negativ." << endl;
    else{
        if (v==0) cout << "A szam nulla." << endl;
        else cout << "A szam pozitiv." << endl;
    }
    //2. feladat
    int x,y;
    cout << "Kerek ket egesz szamot 12 15 alakban: ";
    cin >> x >> y;
    if (x>y)
        cout << y << ' ' << x << endl;
    else {
        if (x==y) cout << x << endl;
        else cout << x << ' ' << y << endl;
    }
    //3. feladat
    int tav, fizetes;
    cout << "Kerek egy tavolsagot (1-30): ";
    cin >> tav;
    if (tav < 3) fizetes=500;
    else {
        if (tav < 6) fizetes=700;
        else {
            if (tav < 11) fizetes=900;
            else {
                if (tav < 21) fizetes = 1400;
                else fizetes = 2000;
            }
        }
    }
    cout << "Dijazas: " << fizetes << " Ft." << endl;
    //4. feladat
    int sz, h;
    float ado;
    cout << "A telek hosszusaga es szelessege 12 15 alakban: ";
    cin >> h >> sz;
    cout << "Ado kedvezmeny elott: ";
    cin >> ado;
    if (sz <= 15 || h <= 25) ado*=0.8;
    cout << "Kedvezmenyes ado: " << ado << endl;
    //5. feladat
    float a,b,c;
    cout << "Kerem a 3 szakasz hosszat 10 12 15 alakban: ";
    cin >> a >> b >> c;
    if (a+b>c && a+c> b && b+c>a)
        cout << "Szerkesztheto haromszog." << endl;
    else
        cout << "Nem szerkesztheto haromszog."  << endl;
}
