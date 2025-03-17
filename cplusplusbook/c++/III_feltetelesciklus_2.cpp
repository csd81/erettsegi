#include <iostream>

using namespace std;

int main(){
    int a,b,c,d;
    do {
        cout << "Irjuk be a ket szamot xx yy alakban: ";
        cin >> a >> b;
    } while (a<=0 || b<=0);
    c=a;
    d=b;
    while (c!=d) {
        if (c>d) d+=b;
        else c+=a;
    }
    cout << "A legkisebb kozos tobbszoros: " << c;
}
