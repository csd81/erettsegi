#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>

using namespace std;

const int n = 20;
int a[n];

void feltolt(){
    srand(time(NULL));
    for(int i=0;i<=n-1;i++)
        a[i]=rand()%999 + 2;
}
void kiir(){
    for (int i=0;i<=n-1;i++)
        cout << a[i] << endl;
    cout << endl;
}
bool prim(int a){
    int i=2;
    while (i<=sqrt(a) && (a % i != 0))
        i++;
    return !(i<=sqrt(a));
}
void primpakol(){
    int e=0;
    int v=n-1;
    int s=a[0];
    while (e < v){
        while (e < v && !(prim(a[v])))
            v--;
        if (e < v){
            a[e] = a[v];
            e++;
            while (e<v && prim(a[e]))
                e++;
            if (e<v){
                a[v]=a[e];
                v--;
            }
        }

    }
    a[e]=s;
}
int main(){
    feltolt();
    kiir();
    primpakol();
    kiir();
}
