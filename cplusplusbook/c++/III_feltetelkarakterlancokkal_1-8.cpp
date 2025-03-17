#include <iostream>
#include <string>

using namespace std;

int main(){
    //1. feladat
    char szj;
    cout << "Kerek egy karaktert: " ;
    cin >> szj;
    if (szj>='0' && szj<='9') cout << "Szamjegy.";
    else cout << "Nem szamjegy.";
    //2. feladat
    char betu;
    cout << endl << "Kerek egy karaktert: " ;
    cin >> betu;
    if ((betu>='a' && betu<='z') || (betu>='A' && betu<='Z'))
        cout << "betu";
    else cout << "nem betu";
    //3. feladat
    string szo;
    cout << endl << "Kerek egy szot: " ;
    cin >> szo;
    if (szo[0] == 'e') cout << "e betuvel kezdodik";
    else cout << "Nem e betuvel kezdodik";
    //4. feladat
    cout << endl << "Kerek egy szot: " ;
    cin >> szo;
    string mgh ="aeiouAEIOU";
    if ( mgh.find(szo[0]) != string::npos) cout << "Maganhangzoval kezdodik.";
    else cout << "Nem maganhangzoval kezdodik.";
    //5. feladat
    string szo1, szo2;
    cout << endl << "Kerek ket szot xxx yyy alakban: " ;
    cin >> szo1 >> szo2;
    if (szo1.length()>szo2.length()) cout << szo2 << ' ' << szo1;
    else cout << szo1 << ' ' << szo2;
    //6. feladat
    cout << endl << "Kerek ket otbetus szot xxx yyy alakban: " ;
    cin >> szo1 >> szo2;
    if (szo1 > szo2) cout << szo2 << ' ' << szo1;
    else cout << szo1 << ' ' << szo2;
    //7. feladat
    cout << endl << "Kerek ket otbetus szot xxx yyy alakban: " ;
    cin >> szo1 >> szo2;
    if (szo1.substr(1,3) > szo2.substr(1,3)) cout << szo2 ;
    else cout << szo1 ;
    //8. feladat
    string szoveg="komor komondorok utaljak a vizsgazo vizslakat";
    cout << endl << szoveg;
    cout << endl << "Kerek egy szot: " ;
    cin >> szo;
    if (szoveg.find(szo) != string::npos) cout << "megtalalhato" ;
    else cout << "nem talalhato meg" ;
}
