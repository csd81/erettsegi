#include <iostream>

using namespace std;

int main(){
    //a - b) feladat
    string orarend[4][5] = {
        {"iras","olvasas","szamtan","rajz","enek"},
        {"olvasas","szamtan","rajz","iras","enek"},
        {"szamtan","olvasas","szamtan","iras","gyak"},
        {"iras","olvasas","szamtan","gyak","szamtan"}
    };
    //c) feladat
    cout << "szerda 3. ora: " << orarend[2][2] << endl;
    //d) feladat
    int n,o;
    cout << "Nap es ora sorszama 1 1 alakban: ";
    cin >> n >> o;
    string napok[7] = {"hetfo","kedd","szerda","csutortok",
                        "pentek", "szombat", "vasarnap"};
    cout << endl << napok[n-1] << ' ' << o << ". ora: ";
    string ora = orarend[o-1][n-1];
    cout << ora << '.' << endl;
    //e) feladat
    string csere;
    csere = orarend[3][0];
    orarend[3][0] = orarend[2][2];
    orarend[2][2] = csere;

}
