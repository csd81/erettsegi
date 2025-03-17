#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int i,j,k;
    streambuf *eredeti = cout.rdbuf();
    fstream ki("szorzotabla.txt",ios::out);
    for(k=0;k<=1;k++){
        if (k==0) cout.rdbuf(ki.rdbuf());
        for(i=1;i<=15;i++){
            for(j=1;j<=15;j++)
                cout << i*j << ' ';
            cout << endl;
        }
        if (k==0) cout.rdbuf(eredeti);
    }
    ki.flush();
    ki.close();
}
