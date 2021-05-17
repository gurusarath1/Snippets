#include <iostream>


class testClass {

        public:
                static int objCount;

                int x,y;

                testClass() {
                        objCount++;
                        std::cout << "Object was created " << "objCount = " << objCount << std::endl;
                }

                testClass(int x){
                        objCount++;
                        std::cout << "Object was created x = "<< x << " objCount = " << objCount << std::endl;
                }

                ~testClass() {
                        objCount--;
                        std::cout << "Object destroyed\n";
                }
};

int testClass::objCount = 0; // Static class variable must be initialized


int main() {

        int* int_ptr = new int;
        int* int_ptr2 = new int;
        int* int_ary = new int[5];

        *int_ptr = 9;
        *int_ptr2 = 8;

        int_ary[0] = 11;
        int_ary[1] = 22;
        int_ary[2] = 33;

        std::cout << *int_ptr << std::endl;
        std::cout << *int_ptr2 << std::endl;
        std::cout << int_ary[0] << "  " << int_ary[1] << "  " << int_ary[2] << std::endl;

        delete int_ptr;
        delete int_ptr2;
        delete[] int_ary;

        testClass x = testClass(); // Object created in stack

        // Object created in heap
        testClass* heap_obj1 = new testClass;
        testClass* heap_obj2 = new testClass();
        testClass* heap_obj3 = new testClass(919);
        testClass* heap_ary = new testClass[3];

        delete heap_obj1;
        delete heap_obj2;
        delete heap_obj3;
        delete[] heap_ary;

        testClass* heap_obj4 = (testClass*) malloc(sizeof(testClass)); // Constructor will not be called

        free(heap_obj4);

        return 0;

}


/*
OUTPUT

9
8
11  22  33
Object was created objCount = 1
Object was created objCount = 2
Object was created objCount = 3
Object was created x = 919 objCount = 4
Object was created objCount = 5
Object was created objCount = 6
Object was created objCount = 7
Object destroyed
Object destroyed
Object destroyed
Object destroyed
Object destroyed
Object destroyed
Object destroyed

*/

