#include <iostream>
#include <fstream>

using namespace std;

int r[50][50], g[50][50], b[50][50];

void megjelenit(){
    int i,j;
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
                        else  {
                            if(r[i][j]==0 && g[i][j]==0 && b[i][j]==0)
                                cout << 'F';
                            else cout << '.';
                        }
                    }
                }
            }
        }
        cout << endl;
    }
}
void keret(){
    int i,j;
    for(i=0;i<=49;i++)
        for(j=0;j<=2;j++){
            r[i][j] = 0;
            g[i][j] = 0;
            b[i][j] = 0;
            r[i][j+47] = 0;
            g[i][j+47] = 0;
            b[i][j+47] = 0;
            r[j][i] = 0;
            g[j][i] = 0;
            b[j][i] = 0;
            r[j+47][i] = 0;
            g[j+47][i] = 0;
            b[j+47][i] = 0;
        }


}
int main(){
    int i,j;
    fstream be("kep.txt",ios::in);
    for(i=0;i<=49;i++)
        for(j=0;j<=49;j++)
            be >> r[i][j] >> g[i][j] >> b[i][j];
    be.close();
    megjelenit();
    keret();
    megjelenit();
}
