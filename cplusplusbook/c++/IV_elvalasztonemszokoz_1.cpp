#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(){
    string kolyokstr, felnottstr, barmi;
    stringstream ks, fs;
    int felnott,kolyok;
    fstream be("veetel_e.txt",ios::in);
    getline(be,felnottstr,'/');
    getline(be,kolyokstr,' ');
    while (!be.eof()){
        getline(be,barmi);
        fs.clear();
        ks.clear();
        fs << felnottstr;
        ks << kolyokstr;
        fs >> felnott;
        ks >> kolyok;
        cout << felnott+kolyok << endl;
        getline(be,felnottstr,'/');
        getline(be,kolyokstr,' ');
    }
    be.close();
}
