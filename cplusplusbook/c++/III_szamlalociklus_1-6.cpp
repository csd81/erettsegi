#include <iostream>

using namespace std;

int main(){
    //1. feladat;
    int i;
    for(i=1;i<=10;i++)
        cout << "Hello vilag!" << endl;
    cout << endl;
    //2. feladat;
    for(i=1;i<=10;i++)
        cout << i << ". Hello vilag!" << endl;
    cout << endl;
    //3. feladat;
    for(i=1;i<=10;i++)
        cout << 2*i << ' ';
    cout << endl;
    //4. feladat;
    for(i=100;i>=0;i-=10)
        cout << i << ' ';
    cout << endl;
    //5. feladat;
    for(i=1;i<=50;i++)
        cout << i % 10;
    cout << endl << endl;
    //6. feladat;
    for(i=1;i<=50;i++)
        cout << i / 10;
    cout << endl;
    for(i=1;i<=50;i++)
        cout << i % 10;
    cout << endl;
}
