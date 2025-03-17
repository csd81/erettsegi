#include <iostream>

using namespace std;

int main(){
    int i,j;
    cout << "   ";
    for (i=1;i<=50;i++)
        cout << i /10;
    cout << endl;
    cout << "   ";
    for (i=1;i<=50;i++)
        cout << i %10;
    cout << endl;
    cout << endl;
    for (i=1;i<=50;i++){
        cout << i/10 << i % 10 << ' ';
        for (j=1;j<=50;j++){
            if ((i % 2 ==1 && j % 2 ==1)||(i % 2 ==0 && j % 2 ==0))
                cout << 'B';
            else cout << 'W';
        }
        cout << endl;
    }
}
