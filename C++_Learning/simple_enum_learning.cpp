#include <iostream>

/*

SYNTAX

enum enum_name { List of names };

enum enum_name : integer_type {  List of names  };

*/


enum errorLevel { SAFE, MODERATE, CRITICAL };
enum logLevel { NO = 5, LOW, MID, HIGH };
enum securityLevel { BAD = 7, OK = 1, GOOD = 3 };

enum testEnum : char {
        zero, one, two, three, four
};

enum test : unsigned char {
        x, y, z, a, b
};

/* ERROR - enum must be int type
enum test : float {
        x, y, z, a, b
};
*/

int main() {


        std::cout << MODERATE << std::endl; // 1
        std::cout << MID << std::endl; // 7
        std::cout << GOOD << std::endl; // 3
        std::cout << four << std::endl; //4

        return 0;
}


