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
	while(p != m1.end()) {
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
	while(p != m1.end()) {
		cout << p->first << "\t" << p->second << "\n";
		p++;
	}
	cout << "\n";

	cout << "----------------------------------\n";

	if(m1.empty()) {
		cout << "m1 is empty\n";
	} else {
		cout << "m1 is not empty\n";
	}

	cout << "Max size of m1 = " << m1.max_size() << "\n";

	m1.clear(); // Remove all elements from m1

	cout << "Size of m1 (After erase) : " << m1.size() << "\n";

	cout << "=================== Part 2 (Different ways to insert elements) ===================" << endl;

	map<char, int> newMap;

	newMap.insert(pair<char, int>('x', 0));
	newMap.insert({'a',1});
	newMap.insert({'b',2});
	newMap['c'] = 3;

	auto iter_obj = newMap.begin();

	while(iter_obj != newMap.end()) {
		cout << iter_obj->first << " : " << iter_obj->second << endl;
		iter_obj++;
	}

	cout << "=================== Check if a key is present ===================" << endl;

	if(newMap.find('a') != newMap.end()) {
		cout << "Key found | " << "Value = " << newMap['a'] << endl;
	} else {
		cout << "Key not found \n";
	}

	if(newMap.find('m') != newMap.end()) {
		cout << "Key found | " << "Value = " << newMap['m'] << endl;
	} else {
		cout << "Key not found \n";
	}

	cout << "=================== Removing an element ===================" << endl;

	newMap.erase('b'); // Erasing by key

	iter_obj = newMap.begin();

	while(iter_obj != newMap.end()) {
		cout << iter_obj->first << " : " << iter_obj->second << endl;
		iter_obj++;
	}



}
