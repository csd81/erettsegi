#include <iostream>

using namespace std;

void elvalaszto(string feladat){
    for(int i=1;i<=80;i++)
        cout << '-';
    cout << feladat << ". feladat"  << endl << endl;
}
int main(){
    elvalaszto("3");
    elvalaszto("b");
    elvalaszto("3.b");
}
