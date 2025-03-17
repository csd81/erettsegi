#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

struct Uzenet {
    int ora;
    int perc;
    string kuldo;
    string szoveg;
};

// Function to read messages from a file
vector<Uzenet> F1(const string& filename) {
    vector<Uzenet> uzenetek;
    ifstream file(filename);
    
    if (!file) {
        cerr << "Hiba: Nem lehet megnyitni a fájlt: " << filename << endl;
        return uzenetek;
    }

    int uzenet_szam;
    file >> uzenet_szam;
    file.ignore(); // Ignore newline after the number

    for (int i = 0; i < uzenet_szam; ++i) {
        Uzenet u;
        file >> u.ora >> u.perc >> u.kuldo;
        file.ignore(); // Ignore the newline after sender
        getline(file, u.szoveg);
        uzenetek.push_back(u);
    }

    return uzenetek;
}

int main() {
    string filename = "input.txt"; // Replace with your actual file name
    vector<Uzenet> messages = F1(filename);

    // Print messages for verification
    for (const auto& u : messages) {
        cout << u.ora << ":" << u.perc << " " << u.kuldo << " -> " << u.szoveg << endl;
    }

    return 0;
}

/*

1.  Olvassa be az `sms.txt` állományban talált adatokat, s annak
    felhasználásával oldja meg a következő feladatokat! Ha az állományt
    nem tudja beolvasni, akkor a benne található adatok közül az első
    tíz üzenet adatait jegyezze be a programba, s úgy oldja meg a
    feladatokat!
2.  A fájlban tárolt utolsó üzenet érkezésekor melyik üzenet a
    legfrissebb a telefon memóriájában? Írja az üzenet szövegét a
    képernyőre!
3.  Adja meg a leghosszabb és a legrövidebb üzenetek adatait! Ha több
    azonos hosszúságú üzenet van, akkor elegendő csak egyet-egyet
    megadnia! A képernyőn óra, perc, telefonszám, üzenet formában
    jelenítse meg az adatokat!
4.  Készítsen karakterhossz szerinti statisztikát:
    `1-20, 21-40, 41-60, 61-80, 81-100`! Az intervallumok mellé a
    hozzájuk tartozó üzenetek darabszámát írja, mint eredményt a
    képernyőre!
5.  Ha Ernő minden óra 0. percében elolvasná a memóriában lévő
    üzeneteket (az éppen ekkor érkező üzeneteket nem látja), majd ki is
    törölné, akkor hány olyan üzenet lenne, amelynek elolvasásához fel
    kellene hívnia a szolgáltatót? Írja ezt a számot a képernyőre! (Az
    üzeneteket először 1, utoljára 24 órakor olvassa el.)
6.  Ernő barátnője gyakran küld sms-t az 123456789-es számról. Mennyi
    volt a leghosszabb idő, amennyi eltelt két üzenete között? Ha
    legfeljebb 1 üzenet érkezett tőle, akkor írja ki, hogy „nincs
    elegendő üzenet", egyébként pedig adja meg a leghosszabb időtartamot
    óra perc alakban!
7.  Egy üzenet véletlenül késett. Olvassa be a billentyűzetről ennek az
    sms-nek az adatait, majd tárolja el a memóriában a többihez
    hasonlóan!
8.  Az `smski.txt` állományban készítsen egy listát az üzenetekről
    telefonszám szerinti csoportosításban, telefonszám szerint növekvő
    sorrendben! Egy csoporthoz tartozó első sorban a feladó telefonszáma
    szerepeljen! Az alatta lévő sorokban a feladás ideje, majd a tőle
    újabb szóközzel elválasztva az üzenet szövege szerepeljen!
*/