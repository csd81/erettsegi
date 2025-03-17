#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    //6. feladat
    char amoba[3][3] = {
        {'X','X','O' },
        {'.','O','O' },
        {'.','O','X' },
    };
    int i,j;
    for(i=0;i<=2;i++){
        for(j=0;j<=2;j++)
            cout << amoba[i][j];
        cout << endl;
    }
    //7. feladat
    cout << endl;
    srand(time(NULL));
    int amobanagy[20][20];
    char fig[3]={'O','X','.'};
    for(i=0;i<=19;i++)
        for(j=0;j<=19;j++)
            amobanagy[i][j]=rand()%3;
    for(i=0;i<=19;i++){
        for(j=0;j<=19;j++)
            cout << fig[amobanagy[i][j]];
        cout << endl;
    }
}
