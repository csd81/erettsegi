#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

int main(){
    //1. feladat
    float x,y,z;
    cout << "Kerek harom egesz szamot 12 10 15 alakban: ";
    cin >> x >> y >> z;
    float atlag = (x+y+z)/3;
    cout << "Az atlag: " << fixed << setprecision(2) << atlag << endl << endl;
    //2. feladat
    float a,b,c;
    cout << "Kerem a haromszog ket befogojat 12 10 alakban: ";
    cin >> a >> b;
    c = sqrt(a*a + b*b);
    cout << "Az atfogo: " << fixed << setprecision(1) << c << endl << endl;
    //3. feladat
    float h,t;
    cout << "Milyen magasrol esik a ko (meter): ";
    cin >> h;
    t = sqrt(2*h/9.81);
    cout << "Az esese " << fixed << setprecision(1) << t
         << " masodpercig tart." << endl << endl;
}
