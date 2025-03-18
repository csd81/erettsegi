#include <iostream>
#include <vector>
#include <algorithm> // required for std::fill

int main() {
    std::vector<int> vec(5);
    std::fill(vec.begin(), vec.end(), 10);
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    return 0;
}
/*
The output of the program is:
10 10 10 10 10
Explanation: The std::fill function is used to fill a range of elements in a container with a specific value. 
In this case, the vector vec is filled with the value 10 using 
std::fill(vec.begin(), vec.end(), 10). 
The for loop then prints out each element of the vector, 
resulting in the output 10 10 10 10 10. 
This is because all elements in the vector have been filled with the value 10.
The std::fill function takes three arguments:
1. The beginning of the range to fill (in this case, vec.begin()).
2. The end of the range to fill (in this case, vec.end()).
3. The value to fill the range with (in this case, 10).
*/

