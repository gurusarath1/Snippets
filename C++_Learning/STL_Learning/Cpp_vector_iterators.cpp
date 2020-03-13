#include <iostream>
#include <vector>


using namespace std;

int main()
{

	vector<int> a;
	vector<int>::iterator p;

	a.push_back(10);
	a.push_back(20);
	a.push_back(40);

	p = a.begin();

	while(p != a.end())
	{
		cout << *p << "  ";
		p++;
	}

	return 0;
}

/*
OUTPUT -------
10 20 40
*/


