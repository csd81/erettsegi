#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int r[10][10];
string nevek[20];
int m[20][10][10];
int vege;

bool ehetre(int ssz){
    bool jo=true;
    int i,j;
    i=0;
    while (i<=9 && jo){
        j=0;
        while (j<=9 && ((m[ssz][i][j] == r[i][j]) || (m[ssz][i][j]-11 == r[i][j])))
            j++;
        if (j>9) i++;
        else jo=false;
    }
    return jo;
}

bool johajoszam(int ssz){
    int db=0;
    int i,j;
    for(i=0;i<=9;i++)
        for(j=0;j<=9;j++)
            if (m[ssz][i][j]==11)
                db++;
    return (db==12);
}

bool joszomszed(int ssz, int x, int y){
    bool jo=true;
    int i,j;
    for(i=x-1;i<=x+1;i++)
        for (j=y-1;j<=y+1;j++)
            if (i>=0 && i<=9 && j>=0 && j<=9)
                if (!(i==x && j==y))
                    if (m[ssz][i][j]!=0) jo=false;
    return jo;
}

bool hajokszomszedsaga(int ssz){
    int i,j;
    bool jo=true;
    for (i=0;i<=9;i++)
        for (j=0;j<=9;j++)
            if (m[ssz][i][j]!=0 && !joszomszed(ssz,i,j)) jo=false;
    return jo;
}

bool toronylatdb(int ssz, int x, int y) {
    int i,k;
    k=0;
    for (i=0;i<=9;i++){
        if (m[ssz][x][i]==11) k++;
        if (m[ssz][i][y]==11) k++;
    }
    if (m[ssz][x][y]==k) return true;
    else return false;
}
bool toronylattabla(int ssz){
    int i,j;
    bool jo=true;
    for(i=0;i<=9;i++)
        for(j=0;j<=9;j++)
            if (m[ssz][i][j]>=1 && m[ssz][i][j]<=9 && !toronylatdb(ssz,i,j)) jo=false;
    return jo;
}

int main(){
    int i,j,k;
    cout << "1. feladat" << endl;
    int s,o,h;
    cout << "Kerem a hajo adatait sor oszlop hajok alakban: ";
    cin >> s >> o >> h;
    if (h>3) cout << "Nehez torony!" << endl;
    cout << "2. feladat" << endl;
    for (i=-1;i<=1;i++)
        for (j=-1;j<=1;j++)
            if (!(i==0 && j==0)) cout << i+s << ' ' << j+o << endl;
    stringstream ss;
    string szstr;
    fstream be("feladvany.txt",ios::in);
    for(i=0;i<=9;i++) {
        for(j=0;j<=8;j++) {
            getline(be,szstr,' ');
            ss.clear();
            ss << szstr;
            ss >> r[i][j];
        }
        getline(be,szstr);
        ss.clear();
        ss << szstr;
        ss >> r[i][j];
    }
    be.close();
    fstream be2("megoldas.txt",ios::in);
    be2 >> vege;
    for(k=0;k<=vege-1;k++){
         be2 >> nevek[k];
         for(i=0;i<=9;i++) {
            for(j=0;j<=8;j++) {
                getline(be2,szstr,' ');
                ss.clear();
                ss << szstr;
                ss >> m[k][i][j];
            }
            getline(be2,szstr);
            ss.clear();
            ss << szstr;
            ss >> m[k][i][j];
        }
    }
    be2.close();
    cout << "3. feladat" << endl;
    cout << "Nem erre a hetre erkeztek: ";
    for(i=0;i<=vege-1;i++)
        if (!ehetre(i)) cout << nevek[i] << ' ';
    cout << endl << "4. feladat" << endl;
    int db = 0;
    for(i=0;i<=vege-1;i++)
        if (ehetre(i) && !johajoszam(i))
            db++;
    cout << "Hajo szama miatt rossz feladvanyok szama: "<< db << " db" << endl;
    cout << "5. feladat" << endl;
    int szomszeddb=0;
    for (i=0;i<=vege-1;i++)
        if (johajoszam(i) && ehetre(i) && !hajokszomszedsaga(i))
            szomszeddb++;
    cout << "Szomszedsag miatt rossz feladvanyok szama: " << szomszeddb << " db" << endl;
    cout << "6. feladat" << endl;
    cout << "Hibatlan megoldasok:\n";
    k=0;
    for (i=0;i<=vege-1;i++)
        if (johajoszam(i) && ehetre(i) && hajokszomszedsaga(i) && toronylattabla(i)){
            cout << nevek[i] << ' ';
            k++;
        }
    cout << endl<< "Ennyi jo megoldas van: " << k << " db";
}
