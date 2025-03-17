#include <iostream>

using namespace std;

bool haromszoge(float a, float b, float c){
    return (a+b>c && a+c> b && b+c>a) ;
}

int main(){
    cout << haromszoge(3,4,10) << endl;
    cout << haromszoge(3,4,5);
}
