#include <iostream>

using namespace std;

void fordit(string szo){
    string seged;
    seged="";
    for(int i=szo.length()-1;i>=0;i--)
        seged+=szo[i];
    szo=seged;
    cout << szo;
}
int main(){
    string beker;
    cout << "Kerek egy szot: ";
    cin >> beker;
    fordit(beker);
}
