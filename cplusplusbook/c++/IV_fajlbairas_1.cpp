#include <iostream>
#include <fstream>

using namespace std;

int main(){
    fstream ki("szuletes.txt",ios::out);
    ki << "Magyary Gyula" << endl;
    ki << "1969.06.09" << endl;
    ki.flush();
    ki.close();
}
