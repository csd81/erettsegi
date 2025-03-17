#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int i,r,g,b;
    fstream be("kep.txt",ios::in);
    for(i=1;i<=2500;i++){
        be >> r >> g >> b;
        cout << "piros: " << r << ", zold: " << g <<", kek: " << b << endl;
    }
    be.close();
}
