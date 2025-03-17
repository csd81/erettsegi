#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    //1. feladat
    int a,b;
    cout << "Adjon meg ket egesz szamot 12 15 formaban: ";
    cin >> a >> b;
    cout << "A kert terulete " << a*b << " negyzetmeter. "
         << 2*(a+b) << " metert kell gyalogolnia a kert korbejarasahoz."
         << endl << endl;
    //2. feladat
    int egesz;
    cout << "paros/paratlan" << endl;
    cout << "Kerek egy egesz szamot: ";
    cin >> egesz;
    cout << endl << egesz % 2 << endl << endl;
    //3. feladat
    int ketjegyu;
    cout << "Kerek egy ketjegyu egesz szamot: ";
    cin >> ketjegyu;
    cout << "Egyesek helyen all: " << ketjegyu % 10 << endl;
    //4. feladat
    cout << "Tizesek helyen all: " << ketjegyu / 10 << endl << endl;
    //5. feladat
    int haromjegyu;
    cout << "Kerek egy ketjegyu egesz szamot: ";
    cin >> haromjegyu;
    cout << "A haromjegyu egyesei: " << haromjegyu % 10;
    cout << ", tizesei: " << (haromjegyu % 100) / 10;
    cout << ", szazasai " << haromjegyu / 100 << '.' << endl << endl;
    //6. feladat
    cout << 24 << '/' << 6 << " = " << 24/6 << endl;
    //7. feladat
    cout << 24 << '/' << 32 << " = " << 24/8 << '/' << 32/8 << endl << endl;
    //8. feladat
    int sz;
    cout << "Kerek egy egesz szamot: ";
    cin >> sz;
    sz=sz+1;
    cout << sz << endl;
    sz=sz+3;
    cout << sz << endl;
    sz=sz+10;
    cout << sz << endl;
    sz=sz+100;
    cout << sz << endl <<endl;
    //9. feladat
    cout << "Kerek egy egesz szamot: ";
    cin >> sz;
    sz--;
    cout << sz << endl;
    sz-=3;
    cout << sz << endl;
    sz-=10;
    cout << sz << endl;
    sz-=100;
    cout << sz << endl <<endl;
    //10. feladat
    int x,y;
    cout << "Kerek ket egesz szamot 12 15 alakban: ";
    cin >> x >> y;
    x+=y;
    cout << x << endl;
    x-=y;
    cout << x << endl;
    x*=y;
    cout << x << endl <<endl;
    //11. feladat
    cout << "dobokocka" << endl;
    srand(time(NULL));
    cout << rand()%6+1 << endl;
    cout << rand()%6+1 << endl << endl;
    //12. feladat
    cout << "fej/iras" << endl;
    srand(time(NULL));
    cout << rand()%2 << endl;
    cout << rand()%2 << endl;
    cout << rand()%2 << endl << endl;

}
