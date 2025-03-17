#include <iostream>

using namespace std;

int main(){
    int a,b,c,d;
    cout << "Irjuk be a ket szamot xx yy alakban: ";
    cin >> a >> b;
    c=a;
    d=b;
    while (c!=d) {
        if (c>d) d+=b;
        else c+=a;
    }
    cout << "A legkisebb kozos tobbszoros: " << c;
}
