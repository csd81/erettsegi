#include <iostream>

using namespace std;

int main(){
    //a - b) feladat
    int kar[11] = {6,5,8,7,10,3,1,2,0,4,9};
    //c) feladat
    cout << "A 7. tanulo a " << kar[7] << ". tanulonak adott ajandekot." << endl;
    //d) feladat
    cout << "d) "<< kar[kar[7]] << endl;
    //e) feladat
    int csere;
    csere = kar[3];
    kar[3] = kar[4];
    kar[4] = csere;
    //f) feladat
    string nev[11] = {"Andras","Bela","Cecilia","Dora","Elemer",
                        "Fanni","Gloria","Hedvig","Ilona",
                        "Jozsef", "Katalin"};
        //g) feladat
        int ssz;
        cout << "Kerem egy tanulo sorszamat (0-10) :";
        cin >> ssz;
        cout << endl << nev[ssz] << ' ' << nev[kar[ssz]]
             << "-t ajandekozta meg." << endl;
        //h) feladat
        cout << nev[ssz] << " -> " << nev[kar[ssz]] << " -> "
             << nev[kar[kar[ssz]]];

}
