#include <iostream>

using namespace std;

int main(){
    int i,n;
    cout << "Adjon meg egy pozitiv egeszet: ";
    cin >> n;
    i=2;
    while (i*i<=n && n % i != 0) i++;
    if (i*i>n) cout << "prim" ;
    else cout << "nem prim";
}
