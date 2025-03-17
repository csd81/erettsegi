#include <iostream>
#include <string>

using namespace std;

int main(){
    //1. feladat
    string szo;
    cout << "Kerek egy szot: " ;
    cin >> szo;
    int h = szo.length();
    cout << endl << "A szo hossza: " << h <<" karakter." << endl;
    //2. feladat
    cout << "A szo kezdobetuje: " << szo[0] << '.' << endl;
    //3. feladat
    cout << "A szo utolso betuje: " << szo[h-1] << '.' << endl;
    //4. feladat
    cout << "Kerek egy otbetus szot: ";
    cin >> szo;
    cout << "A szo kozepso 3 betuje: " << szo.substr(1,3) << '.' << endl;
    //5. feladat
    cout << "Kerek egy budapesti iranyitoszamot: ";
    cin >> szo;
    cout << "A kerulet: " << szo.substr(1,2) << '.' << endl;
    //6. feladat
    string str="leszel";
    str[0]='L';
    cout << str << endl;
    str[str.length()-1]='k';
    cout << str << endl;
    str = str.erase(0,1);
    str = str.erase(str.length()-1,1);
    cout << str << endl;
    str = str.insert(str.length(),"m");
    cout << str << endl;
    //7. feladat
    string vnev,knev;
    cout << "Kerek egy elo- és utonevet xxx yyy formaban: ";
    cin >> vnev >> knev;
    cout << vnev[0]+knev << endl;
    //8. feladat
    cout << vnev.substr(0,3)+knev.substr(0,3)+"01";



}
