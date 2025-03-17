#include <iostream>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int main(){
    //1. feladat
    int sz, n;
    cout << "Kerem a tort szamlalojat es nevezojet 12 15 alakban: ";
    cin >> sz >> n;
    cout << sz << '/' << n << " = " << sz/n << " egesz "
         << sz-(n*(sz/n)) << '/' << n << " = " << (float)sz/(float)n << endl;
    //2. feladat
    cout << "Kerek egy 10..15 szamot: ";
    cin >> sz;
    cout << "A szam hexadecimalis alakja: " << (char)(sz+55) << endl;
    //3. feladat
    cout << "Kerek egy a..f hexadecimalis szamot: ";
    char h;
    cin >> h;
    cout << "A szam decimalis alakja: " << (int)h-87 << endl;
    //4. feladat
    string str1, str2;
    cout << "Kerem az elso karakterlancot (xxszoveg) ";
    cin >> str1;
    cout << "Kerem a masodik karakterlancot (yyszoveg) ";
    stringstream s1, s2;
    cin >> str2;
    s1 << str1.substr(0,2);
    s2 << str2.substr(0,2);
    int elso, masodik;
    s1 >> elso;
    s2 >> masodik;
    cout << "A szamok osszege: " << elso+masodik << endl;
    //5. feladat
    srand(time(NULL));
    cout << "Veletlen kisbetu: " << (char)(rand()%25+97);
}
