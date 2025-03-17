#include <iostream>

using namespace std;

int main(){
    int i,j;
    for (i=1;i<=50;i++){
        for (j=1;j<=51-i;j++)
            cout << '.';
        cout << endl;
    }
}
