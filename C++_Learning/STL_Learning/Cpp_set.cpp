#include <iostream>
#include <set>

using namespace std;

int main()
{

    set<int> setX;
    
    setX.insert(5);
    setX.insert(1);
    setX.insert(2);
    setX.insert(2);
    setX.insert(5);
    
    for(int i : setX) {
        cout << i << "   ";
    }
    
    cout << endl;
    
    // Delete an element
    setX.erase(2);
    
    for(int i : setX) {
        cout << i << "   ";
    }
    
    cout << endl;
    
    
    // Using iterator
    set<int>::iterator p;
    
    p = setX.begin();
    
    while(p != setX.end()) {
        cout << *p << endl;
        p++;
    }
    
    
    return 0;
}


/*
OUTPUT

1   2   5   
1   5   
1
5

*/
