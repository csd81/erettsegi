#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(){
    string szo;
    cout << "1. feladat" << endl;
    cout << "Kerek egy szot: " ;
    cin >> szo;
    int i=0;
    int h = szo.length();
    while (i<=h-1 && !(szo[i]=='a' || szo[i]=='e' || szo[i]=='i' || szo[i]=='o' || szo[i]=='u')){
        i++;
    }
    if (i>h-1) cout << "Nem tartalmaz maganhangzot";
    else cout << "Tartalmaz maganhangzot";
    cout << endl;
    int maxertek=0;
    string leghosszabbszo="";
    h = 0;
    int dbszo=0;
    int dbtobbmaganh=0;
    string otkarakteres[1000];
    int otkarelemszam=-1;
    cout << endl << "3. feladat" << endl;
    fstream be("szoveg.txt",ios::in);
    be >> szo;
    while (!be.eof()){
        h = szo.length();
        dbszo++;
        if (maxertek < h) {
            maxertek = h;
            leghosszabbszo=szo;
        }
        int db=0;
        for (i=0;i<=h-1;i++)
            if (szo[i]=='a' || szo[i]=='e' || szo[i]=='i' || szo[i]=='o' || szo[i]=='u')
                db++;
        if (db>h-db) {
            dbtobbmaganh++;
            cout << szo << " ";
        }
        if (h == 5){
            otkarelemszam++;
            otkarakteres[otkarelemszam]=szo;
        }
        be >> szo;
    }
    be.close();
    float szazalek = 100*(float)dbtobbmaganh/(float)dbszo;
    cout << endl << dbtobbmaganh << '/' << dbszo << " : ";
    cout << fixed << setprecision(2) << szazalek << "%" << endl;
    cout << endl << "2. feladat" << endl;
    cout << "A leghosszabb szo: " << leghosszabbszo << endl;
    cout << endl << "4. feladat" << endl;
    string harombetus;
    cout << "Kerek egy harombetus szoreszletet: ";
    cin >> harombetus;
    cout << "Hozza tartozo otkarakteres szavak: ";
    for(i=0;i<=otkarelemszam;i++)
        if (otkarakteres[i].substr(1,3)==harombetus)
            cout << otkarakteres[i] << " ";
    cout << endl;
    cout << endl << "5. feladat" << endl;
    int j;
    string csere;
    fstream ki("letra.txt",ios::out);
    for(i=0;i<=otkarelemszam-1;i++)
        for(j=otkarelemszam;j>i;j--)
            if (otkarakteres[j-1].substr(1,3)>otkarakteres[j].substr(1,3)){
                csere = otkarakteres[j];
                otkarakteres[j]=otkarakteres[j-1];
                otkarakteres[j-1]=csere;
            }
    if (otkarakteres[0].substr(1,3)==otkarakteres[1].substr(1,3))
        ki << otkarakteres[0] << endl;
    for(i=1;i<=otkarelemszam-2;i++){
        if (otkarakteres[i].substr(1,3)==otkarakteres[i-1].substr(1,3)
        || otkarakteres[i].substr(1,3)==otkarakteres[i+1].substr(1,3))
            ki << otkarakteres[i] << endl;
        if (otkarakteres[i].substr(1,3)!=otkarakteres[i+1].substr(1,3)
        && otkarakteres[i].substr(1,3)==otkarakteres[i-1].substr(1,3))
            ki << endl;
    }
    if (otkarakteres[i].substr(1,3)==otkarakteres[i+1].substr(1,3))
        ki << otkarakteres[i+1] << endl;
    ki.flush();
    ki.close();
    cout << "Elkeszult a letra.txt fajl.";
}
