#include <iostream>
#include <map>

using namespace std;

int main(){
    string beker;
    cout << "Kerek egy ketjegyu hexadec. szamot (pl. A9): ";
    cin >> beker;
    map <char,int> ertek;
    ertek['0']=0;
    ertek['1']=1;
    ertek['2']=2;
    ertek['3']=3;
    ertek['4']=4;
    ertek['5']=5;
    ertek['6']=6;
    ertek['7']=7;
    ertek['8']=8;
    ertek['9']=9;
    ertek['A']=10;
    ertek['B']=11;
    ertek['C']=12;
    ertek['D']=13;
    ertek['E']=14;
    ertek['F']=15;
    cout << "Tizes szamrendszerben: "
         << 16*ertek[beker[0]]+ertek[beker[1]];
}
