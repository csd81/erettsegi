#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    srand(time(NULL));
    int szam = rand()%7+1;
    switch (szam){
        case 1:
            cout <<"   " << endl;
            cout <<" O " << endl;
            cout <<"   " << endl;
            break;
        case 2:
            cout <<"O  " << endl;
            cout <<"   " << endl;
            cout <<"  O" << endl;
            break;
        case 3:
            cout <<"O  " << endl;
            cout <<" O " << endl;
            cout <<"  O" << endl;
            break;
        case 4:
            cout <<"O O" << endl;
            cout <<"  " << endl;
            cout <<"O O" << endl;
            break;
        case 5:
            cout <<"O O" << endl;
            cout <<" O " << endl;
            cout <<"O O" << endl;
            break;
        case 6 : case 7:
            cout <<"O O" << endl;
            cout <<"O O" << endl;
            cout <<"O O" << endl;
            break;
    }
}
