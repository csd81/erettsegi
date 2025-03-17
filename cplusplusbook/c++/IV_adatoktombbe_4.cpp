#include <iostream>
#include <fstream>

using namespace std;

int main(){
    struct kepek {
        int r;
        int g;
        int b;
    };
    int i,j;
    kepek kep[50][50];
    fstream be("kep.txt",ios::in);
    for(i=0;i<=49;i++)
        for(j=0;j<=49;j++)
            be >> kep[i][j].r >> kep[i][j].g >> kep[i][j].b;
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
            if(kep[i][j].r==255 && kep[i][j].g==0 && kep[i][j].b==0)
                cout << 'P';
            else {
                if(kep[i][j].r==0 && kep[i][j].g==255 && kep[i][j].b==0)
                    cout << 'Z';
                else {
                    if(kep[i][j].r==0 && kep[i][j].g==0 && kep[i][j].b==255)
                        cout << 'K';
                    else {
                        if(kep[i][j].r==255 && kep[i][j].g==255 && kep[i][j].b==0)
                            cout << 'S';
                        else cout << '.';
                    }
                }
            }
        }
        cout << endl;
    }
}
