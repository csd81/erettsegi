#include <iostream>

using namespace std;

int fizet(int tav){
    int fizetes;
    if (tav < 3) fizetes=500;
    else {
        if (tav < 6) fizetes=700;
        else {
            if (tav < 11) fizetes=900;
            else {
                if (tav < 21) fizetes = 1400;
                else fizetes = 2000;
            }
        }
    }
    return fizetes;
}

int main(){
    int km;
    cout << "Kerek egy tavolsagot (1-30): ";
    cin >> km;
    cout << "Dijazas: " << fizet(km) << " Ft." << endl;
}
