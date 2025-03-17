#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int i,j,sz;
    int r[2500], g[2500], b[2500];
    fstream be("kep.txt",ios::in);
    for(i=0;i<=2499;i++)
        be >> r[i] >> g[i] >> b[i];
    be.close();
    cout << "   ";
    for(i=0;i<=49;i++)
        cout << i / 10;
    cout << endl << "   ";
    for(i=0;i<=49;i++)
        cout << i % 10;
    cout << endl << endl;
    for(i=0;i<=49;i++){
        cout << i / 10 << i % 10 << ' ';
        for(j=0;j<=49;j++){
            sz = i*50 + j;
            if(r[sz]==255 && g[sz]==0 && b[sz]==0)
                cout << 'P';
            else {
                if(r[sz]==0 && g[sz]==255 && b[sz]==0)
                    cout << 'Z';
                else {
                    if(r[sz]==0 && g[sz]==0 && b[sz]==255)
                        cout << 'K';
                    else {
                        if(r[sz]==255 && g[sz]==255 && b[sz]==0)
                            cout << 'S';
                        else cout << '.';
                    }
                }
            }
        }
        cout << endl;
    }
}
