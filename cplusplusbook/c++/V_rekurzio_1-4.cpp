#include <iostream>

using namespace std;

int lnko(int a, int b){
    if (a==b) return a;
    if (a<b) return lnko(a,b-a);
    if (a>b) return lnko(a-b,b);
}
int lkkt(int a, int b){
    return a*b/lnko(a,b);
}
int faktor(int n){
    if (n>1) return n*faktor(n-1);
    else return 1;
}
int fib(int n){
    if (n>2) return fib(n-1)+fib(n-2);
    else return 1;
}

int main(){
    cout << lnko(75,120) << endl;
    cout << lkkt(75,120) << endl;
    cout << faktor(4) << endl;
    cout << fib(7) << endl;
}
