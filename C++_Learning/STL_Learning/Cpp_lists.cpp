#include <iostream>
#include <list>

using namespace std;

int main()
{

	list<int> a;
	list<int>::iterator p;

	a.push_back(14);
	a.push_back(75);
	a.push_back(34);
	a.push_back(56);
	a.push_back(6);
	a.push_front(7);
	a.push_front(99);

	p = a.begin();
	while(p != a.end())
	{
		cout << *p << "  ";
		p++;
	}
	cout << "\n";

	a.sort(); // SOrt the list

	p = a.begin();
	while(p != a.end())
	{
		cout << *p << "  ";
		p++;
	}
	cout << "\n";

	list<int> b;
	b.push_back(1000);
	b.push_back(999);

	a.merge(b);  // Merge two lists

	p = a.begin();
	while(p != a.end())
	{
		cout << *p << "  ";
		p++;
	}
	cout << "\n";
	
	return 0;
}

/*
OUTPUT --------------

99  7  14  75  34  56  6
6  7  14  34  56  75  99
6  7  14  34  56  75  99  1000  999
*/