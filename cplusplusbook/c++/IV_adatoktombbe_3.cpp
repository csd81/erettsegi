#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int i,j;
    int r[50][50], g[50][50], b[50][50];
    fstream be("kep.txt",ios::in);
    for(i=0;i<=49;i++)
        for(j=0;j<=49;j++)
            be >> r[i][j] >> g[i][j] >> b[i][j];
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
            if(r[i][j]==255 && g[i][j]==0 && b[i][j]==0)
                cout << 'P';
            else {
                if(r[i][j]==0 && g[i][j]==255 && b[i][j]==0)
                    cout << 'Z';
                else {
                    if(r[i][j]==0 && g[i][j]==0 && b[i][j]==255)
                        cout << 'K';
                    else {
                        if(r[i][j]==255 && g[i][j]==255 && b[i][j]==0)
                            cout << 'S';
                        else cout << '.';
                    }
                }
            }
        }
        cout << endl;
    }
}
