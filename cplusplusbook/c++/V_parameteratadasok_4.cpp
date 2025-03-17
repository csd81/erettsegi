#include <iostream>

using namespace std;
void csere(int &x, int &y){
    x-=y;
    y+=x;
    x=y-x;
}

int main(){
    int a,b;
    cout << "Kerek ket egesz szamot 12 15 alakban: ";
    cin >> a >> b;
    csere(a,b);
    cout << a << ' ' << b;
}
