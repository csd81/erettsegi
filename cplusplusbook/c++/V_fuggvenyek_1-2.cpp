#include <iostream>

using namespace std;

int faktor(int n){
    int sz=1;
    for(int i=1;i<=n;i++)
        sz*=i;
    return sz;
}

int fib(int n){
    int kisebb, nagyobb, uj;
    kisebb = 1;
    nagyobb = 1;
    if (n>2)
        for (int i=3;i<=n;i++){
            uj = nagyobb + kisebb;
            kisebb = nagyobb;
            nagyobb = uj;
        }
    else uj = 1;
    return uj;
}
int main(){
    cout << faktor(4) << endl;
    cout << fib(7) ;
}
