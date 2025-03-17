#include <iostream>

using namespace std;

void elvalaszto(string feladat, bool fel){
    int n=80;
    if (fel) n/=2;
    for(int i=1;i<=n;i++)
        cout << '-';
    cout << endl << feladat << ". feladat"  << endl << endl;
}
int main(){
    elvalaszto("3",true);
    elvalaszto("b",false);
    elvalaszto("3.b",true);
}
