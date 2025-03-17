#include <iostream>

using namespace std;

void kep(int x, int y){
    int i;
    cout << "  ";
    for (i=1;i<=x;i++)
        cout << i / 10;
    cout << endl;
    cout << "  ";
    for (i=1;i<=x;i++)
        cout << i % 10;
    cout << endl;
    for (i=1;i<=y;i++)
        cout << i / 10 << i % 10 << endl;
}
int main(){
    kep(20,10);
}
