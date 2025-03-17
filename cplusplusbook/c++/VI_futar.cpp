#include <iostream>
#include <fstream>

using namespace std;

int fizet(int tav){
    int fizetes;
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
    return fizetes;
}

int main(){
    struct fuvarok {
        int nap;
        int fuvar;
        int hossz;
    };
    fuvarok rekord[100];
    fuvarok csere;
    int db=0;
    fstream be("tavok.txt",ios::in);
    be >> rekord[0].nap >> rekord[0].fuvar >> rekord[0].hossz;
    while (!be.eof()){
        db++;
        be >> rekord[db].nap >> rekord[db].fuvar >> rekord[db].hossz;
    }
    be.close();
    db--;
    int i,j;
    for(i=0;i<=db-1;i++)
        for(j=db;j>i;j--)
            if (rekord[j-1].nap*100+rekord[j-1].fuvar>rekord[j].nap*100+rekord[j].fuvar){
                csere = rekord[j];
                rekord[j]=rekord[j-1];
                rekord[j-1]=csere;
            }
    cout << "2. feladat " << endl;
    cout << "A het legelso utjanak hossza km-ben: " << rekord[0].hossz << endl;
    cout << "3. feladat " << endl;
    cout << "A het utolso utjanak hossza km-ben: " << rekord[db].hossz << endl;
    cout << db << ' ' << rekord[db].nap << ' ' << rekord[db].fuvar
         << ' ' << rekord[db].hossz;
    cout << "4. feladat" << endl;
    int fsz[8];
    int km[8];
    for(i=1;i<=7;i++){
        fsz[i]=0;
        km[i]=0;
    }
    for(i=0;i<=db-1;i++) {
        km[rekord[i].nap]+=rekord[i].hossz;
        fsz[rekord[i].nap]++;
    }
    cout << "Nem dolgozott ezeken a napokon: ";
    for(i=1;i<=7;i++)
        if (fsz[i]==0)
            cout << i << ". ";
    int maxhely=1;
    int maxnap=fsz[1];
    for(i=2;i<=7;i++)
        if (maxnap<fsz[i]){
            maxnap=fsz[i];
            maxhely=i;
        }
    cout << endl << "5. feladat" << endl;
    cout << "A legtobb fuvar ezen a napon volt: " << maxhely << endl;
    cout << "6. feladat" << endl;
    for(i=1;i<=7;i++)
        cout << i << ". nap: " << km[i] << " km" << endl;
    cout << "7. feladat " << endl;
    int tav;
    cout << "Kerek egy tavot: ";
    cin >> tav;
    cout << "Ennyi fizettseg jar erte forintan: " << fizet(tav) << endl;
    cout << "8. feladat " << endl;
    int osszfiz=0;
    fstream ki("dijazas.txt",ios::out);
    for(i=0;i<=db;i++){
        ki << rekord[i].nap << ". nap " << rekord[i].fuvar
             << ". ut: " << fizet(rekord[i].hossz) << " Ft\n";
        osszfiz+=fizet(rekord[i].hossz);
    }
    ki.flush();
    ki.close();
    cout << "Kesz a dijazas.txt fajl." << endl;
    cout << "9. feladat " << endl;
    cout << "Heti munkajaert a futar ennyi Ft-ot kapott: " << osszfiz;
}
