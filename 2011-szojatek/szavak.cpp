#include <iostream>
#include <fstream>
#include <iomanip>


int main(){
	std::string szo;
	std::cout << "1." << std::endl;
	std::cout << "szo? ";
	std::cin >> szo;
	int i = 0;
	int h = szo.length();
	while (i <= h-1 && !(szo[i] == 'a' || szo[i] == 'e' || szo[i] == 'i' || szo[i] == 'o' || szo[i] == 'u')){
		
		i++;
	}
	if (i <= h-1){
		std::cout << "van benne maganhangzo" << std::endl;
	}
	else{
		std::cout << "nincs benne maganhangzo" << std::endl;
	}


	return 0;
}