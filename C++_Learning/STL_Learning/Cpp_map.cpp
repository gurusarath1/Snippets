#include <iostream>
#include <map>

using namespace std;

int main()
{

	map<char,int> m1;
	map<char,int>::iterator p;

	m1['a'] = 0;
	m1['b'] = 1;
	m1['c'] = 2;

	cout << m1['b'] << "\n";
	
	cout << "KEY" << "\tVALUE\n";
	p = m1.begin();
	while(p != m1.end())
	{
		cout << p->first << "\t" << p->second << "\n";
		p++;
	}
	cout << "\n";

	cout << "Size of m1 : " << m1.size() << "\n";

	cout << m1['d'] << "\n"; // Trying to access an element not present in the map
	// Now 'd' is added to the map

	cout << "Size of m1 (After trying to access 'd') : " << m1.size() << "\n";

	cout << "----------------------------------\n";

	m1.erase('b'); // Removing a key from the map
	// another version of erase: m1.erase(itr position)

	cout << "Remove 'b' \n";
	cout << "KEY" << "\tVALUE\n";
	p = m1.begin();
	while(p != m1.end())
	{
		cout << p->first << "\t" << p->second << "\n";
		p++;
	}
	cout << "\n";

	cout << "----------------------------------\n";

	if(m1.empty())
	{
		cout << "m1 is empty\n";
	} else {
		cout << "m1 is not empty\n";
	}

	cout << "Max size of m1 = " << m1.max_size() << "\n";

	m1.clear(); // Remove all elements from m1

	cout << "Size of m1 (After erase) : " << m1.size() << "\n";

}

/*
OUTPUT ---------------------------------------------

1
KEY     VALUE
a       0
b       1
c       2

Size of m1 : 3
0
Size of m1 (After trying to access 'd') : 4
----------------------------------
Remove 'b'
KEY     VALUE
a       0
c       2
d       0

----------------------------------
m1 is not empty
Max size of m1 = 461168601842738790
Size of m1 (After erase) : 0
*/