#include <iostream>
#include <map>

using namespace std;

int main()
{


    map<char,int> m1;
    
    m1['a'] = 0;
    m1['b'] = 5;
    m1['c'] = 1;
    m1['d'] = 2;
    m1['r'] = 3;
    
    pair<int,int> x;
    x.first = 4;
    x.second = 4;
    
    for(pair<char,int> i : m1) {
        cout << i.first << "   " << i.second << endl;
    }
    
    cout << "--------\n";
    
    map<char, int>::iterator p;
    
    p = m1.begin();
    
    while(p != m1.end()) {
        cout << p->first << "   " << p->second << endl;
        p++;
    }
    

    return 0;
}


/*
OUTPUT

a   0
b   5
c   1
d   2
r   3
--------
a   0
b   5
c   1
d   2
r   3


*/
