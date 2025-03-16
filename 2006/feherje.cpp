#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

const int atomC = 12, atomH = 1, atomO = 16, atomN = 14, atomS = 32;

struct Aminosav {
    string rovid;
    char jel;
    int c, h, o, n, s, molTomeg;
    
    void calculateMolTomeg() {
        molTomeg = c * atomC + h * atomH + o * atomO + n * atomN + s * atomS;
    }
};

vector<Aminosav> aminosavak;
map<char, Aminosav> amino_map;

void betoltes(const string& filename) {
    ifstream be(filename);
    if (!be) {
        cout << "A fájl nem található, alapértelmezett adatokkal dolgozom!\n";
        aminosavak = { {"Gly", 'G', 2, 5, 2, 1, 0},
                       {"Ala", 'A', 3, 7, 2, 1, 0},
                       {"Arg", 'R', 6, 14, 2, 4, 0},
                       {"Phe", 'F', 9, 11, 2, 1, 0},
                       {"Cys", 'C', 3, 7, 2, 1, 1} };
    } else {
        for (int i = 0; i < 20; ++i) {
            Aminosav a;
            be >> a.rovid >> a.jel >> a.c >> a.h >> a.o >> a.n >> a.s;
            aminosavak.push_back(a);
        }
        be.close();
    }
    for (auto &a : aminosavak) {
        a.calculateMolTomeg();
        amino_map[a.jel] = a;
    }
}

void kiiras(const string& szoveg, const string& filename) {
    ofstream ki(filename, ios::app);
    cout << szoveg << endl;
    ki << szoveg << endl;
}

string betoltBSA(const string& filename) {
    ifstream bsa_file(filename);
    if (!bsa_file) return "GARFCGARFCGARFCGARFCGARFCGARFCGARFCGARFCGARFCGARFC";
    string bsa;
    bsa_file >> bsa;
    return bsa;
}

void kiszamolEsKiir(const string& bsa, const string& filename) {
    int C = 0, H = 0, O = 0, N = 0, S = 0;
    for (char ch : bsa) {
        if (amino_map.count(ch)) {
            Aminosav a = amino_map[ch];
            C += a.c; H += a.h; O += a.o; N += a.n; S += a.s;
        }
    }
    int v = bsa.size() - 1;
    H -= 2 * v;
    O -= v;
    kiiras("4. feladat", filename);
    kiiras("C " + to_string(C) + " H " + to_string(H) + " O " + to_string(O) + " N " + to_string(N) + " S " + to_string(S), filename);
}

void keresMaxHidrofob(const string& bsa, const string& filename) {
    int maxHossz = 0, kezdet = 0, vege = 0, tempkezdet = 0;
    for (size_t i = 0; i < bsa.size(); i++) {
        if (bsa[i] == 'Y' || bsa[i] == 'W' || bsa[i] == 'F') {
            if (i - tempkezdet + 1 > maxHossz) {
                maxHossz = i - tempkezdet + 1;
                kezdet = tempkezdet;
                vege = i;
            }
            tempkezdet = i + 1;
        }
    }
    kiiras("5. feladat", filename);
    kiiras("kezdet helye: " + to_string(kezdet + 1) + " vége helye: " + to_string(vege + 1) + " hossza: " + to_string(maxHossz), filename);
}

void szamolCisztein(const string& bsa, const string& filename) {
    int cisztein_db = 0;
    for (size_t i = 0; i < bsa.size() - 1; i++) {
        if (bsa[i] == 'R' && (bsa[i + 1] == 'A' || bsa[i + 1] == 'V')) {
            for (size_t j = 0; j <= i; j++) {
                if (bsa[j] == 'C') cisztein_db++;
            }
            break;
        }
    }
    kiiras("6. feladat", filename);
    kiiras("Az első fehérjelánc részletben " + to_string(cisztein_db) + " Cisztein (C) található!", filename);
}

int main() {
    betoltes("aminosav.txt");
    string bsa = betoltBSA("bsa.txt");
    
    sort(aminosavak.begin(), aminosavak.end(), [](const Aminosav& a, const Aminosav& b) {
        return a.molTomeg < b.molTomeg;
    });
    
    kiiras("3. feladat", "eredmeny.txt");
    for (const auto& a : aminosavak)
        kiiras(a.rovid + " " + to_string(a.molTomeg), "eredmeny.txt");
    
    kiszamolEsKiir(bsa, "eredmeny.txt");
    keresMaxHidrofob(bsa, "eredmeny.txt");
    szamolCisztein(bsa, "eredmeny.txt");
    
    return 0;
}
