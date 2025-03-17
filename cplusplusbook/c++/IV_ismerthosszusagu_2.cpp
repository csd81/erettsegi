#include <iostream>
#include <fstream>

using namespace std;

int main(){
    int i,n,o,p,m,cs,ind,cel;
    fstream be("igeny.txt",ios::in);
    be >> n;
    be >> n;
    be >> n;
    for(i=1;i<=n;i++){
        be >> o >> p >> m >> cs >> ind >> cel;
        cout << cs <<". csapat - indul: " << ind << ". szint, erkezik: "
            << cel << ". szint, " << o << " ora " << p << " perc "
            << m << "mp." << endl;
    }
    be.close();
}
