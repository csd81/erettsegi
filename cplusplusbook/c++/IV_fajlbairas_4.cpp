#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    int i,vel;
    char muv[4] = {'+','-','*','/'};
    srand(time(NULL));
    fstream ki("tortek.txt",ios::out);
    for(i=1;i<=100;i++)
        ki << rand()%99+1 << ' ' << rand()%99+1 << ' '
            << rand()%99+1 << ' ' << rand()%99+1 << ' '
            << muv[rand()%4] << endl;
    ki.flush();
    ki.close();
}
