#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int sz1, n1, sz2, n2;
    char muv;
    fstream be("adat.txt",ios::in);
    be >> sz1 >> n1 >> sz2 >> n2 >> muv;
    while (!be.eof()){
        cout << sz1 << '/' << n1 << ' ' << muv << ' '
             << sz2 << '/' << n2 << " =" << endl;
        be >> sz1 >> n1 >> sz2 >> n2 >> muv;
    }
    be.close();
}
