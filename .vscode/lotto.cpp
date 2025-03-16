#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream be("lottosz.dat");
    ofstream ki("lotto52.ki");

    vector<vector<int>> szamok(51, vector<int>(5));

    for(int i=0; i<51; i++)
        for(int j=0; j<5; j++)
            be >> szamok[i][j];

    vector<int> het52(5);
    cout << "Adja meg az 52. hét lottószámait:" << endl;
    for(int &sz : het52)
        cin >> sz;

    sort(het52.begin(), het52.end());
    cout << "52. hét rendezett számai: ";
    for(int sz : het52) cout << sz << " ";
    cout << endl;

    int sorszam;
    cout << "Adjon meg egy hét sorszámot (1-51): ";
    cin >> sorszam;
    cout << sorszam << ". hét számai: ";
    for(int sz : szamok[sorszam-1]) cout << sz << " ";
    cout << endl;

    vector<int> gyakorisag(91,0);
    for(auto &het : szamok)
        for(int sz : het)
            gyakorisag[sz]++;

    bool volt_kihuzatlan = false;
    for(int i=1; i<=90; i++)
        if(gyakorisag[i]==0)
            volt_kihuzatlan = true;

    cout << (volt_kihuzatlan ? "Van" : "Nincs") << " olyan szám, amit nem húztak ki." << endl;

    int paratlan = 0;
    for(auto &het : szamok)
        for(int sz : het)
            if(sz%2!=0) paratlan++;

    cout << "Páratlan számok darabszáma: " << paratlan << endl;

    // lotto52.ki fájl készítése
    for(auto &het : szamok){
        for(int sz : het)
            ki << sz << " ";
        ki << endl;
    }
    for(int sz : het52)
        ki << sz << " ";
    ki << endl;

    ki.close();

    // 8. feladat: számok gyakorisága
    gyakorisag.assign(91, 0);
    ifstream lotto52("lotto52.ki");
    int tmp;
    while(lotto52 >> tmp)
        gyakorisag[tmp]++;

    for(int i=1; i<=90; i++){
        cout << gyakorisag[i] << "\t";
        if(i%15==0) cout << endl;
    }

    // 9. feladat: prímszámok
    vector<int> primek = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89};
    cout << "Egyszer sem kihúzott prímszámok: ";
    for(int p : primek)
        if(gyakorisag[p]==0)
            cout << p << " ";
    cout << endl;

    return 0;
}