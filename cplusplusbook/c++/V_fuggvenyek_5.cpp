#include <iostream>

using namespace std;

bool prime(int n){
    int i=2;
    while (i*i<=n && n % i != 0) i++;
    return (i*i>n);
}

int main(){
    cout << prime(13) << endl;
    cout << prime(24);
}
