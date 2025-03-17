#include <iostream>

using namespace std;

int main(){
    string szam;
    int t, e;
    cout << "Kerek egy ketjegyu hexadecimalis szamot (00-FF): ";
    cin >> szam;
    switch (szam[0]){
        case 'A': t=10; break;
        case 'B': t=11; break;
        case 'C': t=12; break;
        case 'D': t=13; break;
        case 'E': t=14; break;
        case 'F': t=15; break;
        default:
            t = (int)szam[0]-48;
    }
    switch (szam[1]){
        case 'A': e=10; break;
        case 'B': e=11; break;
        case 'C': e=12; break;
        case 'D': e=13; break;
        case 'E': e=14; break;
        case 'F': e=15; break;
        default:
            e = (int)szam[1]-48;
    }
    cout << t*16+e ;
}
