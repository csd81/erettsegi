#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

struct vetel {
    int nap;
    int amator;
    string vett;
};
vetel uzenet[1000];

bool szame(string szo) {
    bool valasz=true;
    for(int i=0;i<szo.length();i++)
        if (szo[i]<'0' || szo[i]>'9') valasz=false;
    return valasz;
}

int main(){
    fstream be("veetel.txt",ios::in);
    int utolso=0;
    be >> uzenet[0].nap >> uzenet[0].amator;
    getline(be,uzenet[0].vett) ;
    getline(be,uzenet[0].vett) ;
    while (!be.eof()){
        utolso++;
        be >> uzenet[utolso].nap >> uzenet[utolso].amator;
        getline(be,uzenet[utolso].vett) ;
        getline(be,uzenet[utolso].vett) ;
   }
    be.close();
    int nsz, asz, i;
    cout << "Adja meg a nap sorszamat: ";
    cin >> nsz;
    cout << endl << "Adja meg a radioamator sorszamat: "   ;
    cin >> asz;
    i=0;
    while (i<=utolso && !(uzenet[i].nap==nsz && uzenet[i].amator == asz ))
        i++;
    if (i<=utolso) {
        stringstream ss,konv;
        string felnottstr,kolyokstr;
        int felnott, kolyok;
        ss << uzenet[i].vett;
        getline(ss,felnottstr,'/');
        getline(ss,kolyokstr,' ');
        if (szame(felnottstr) && szame(kolyokstr)){
            konv << felnottstr;
            konv >> felnott;
            konv.clear();
            konv << kolyokstr;
            konv >> kolyok;
            cout << "A megfigyelt egyedek szama: " << kolyok+felnott << endl;
        }
        else
            cout << "Nincs informacio.";
    }
    else
        cout << "Nincs ilyen feljegyzes.";
}
