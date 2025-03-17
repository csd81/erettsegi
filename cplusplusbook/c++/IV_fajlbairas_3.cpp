#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(){
    int hsz;
    srand(time(NULL));
    fstream ki("telkek.txt",ios::out);
    for(hsz=1;hsz<=50;hsz++)
        ki << hsz << ' '<< rand()%30+20 << ' ' << rand()%50+50 << endl;
    ki.flush();
    ki.close();
}
