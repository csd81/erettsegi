#include <iostream>

using namespace std;

int main(){
    int a,b;
    cout << "Irjuk be a ket szamot xx yy alakban: ";
    cin >> a >> b;
    while (a>0 && b>0){
        while (a!=b) {
            if (a>b) a-=b;
            else b-=a;
        }
        cout << "A legnagyobb kozos oszto: " << a << endl;
        cout << "Irjuk be a ket szamot xx yy alakban: ";
        cin >> a >> b;
    }

}
