#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int db=0;
    char bazis[1000];
    fstream be("bsa.txt",ios::in);
    be >> bazis[0];
    while (!be.eof()){
        db++;
        be >> bazis[db];
    }
    db--;
    be.close();
    for(int i=db;i>=0;i--)
        cout << bazis[i];
}
