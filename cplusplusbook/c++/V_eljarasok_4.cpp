#include <iostream>

using namespace std;

void kep(){
    int i;
    cout << "  ";
    for (i=1;i<=50;i++)
        cout << i / 10;
    cout << endl;
    cout << "  ";
    for (i=1;i<=50;i++)
        cout << i % 10;
    cout << endl;
    for (i=1;i<=50;i++)
        cout << i / 10 << i % 10 << endl;
}
int main(){
    kep();
}
