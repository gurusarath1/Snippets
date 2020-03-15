#include <iostream>
#include <list>

using namespace std;

void print_list(list<int> a);

int main()
{

	list<int> a;

	a.push_back(1);
	a.push_back(2);
	a.push_back(3);
	a.push_back(4);
	a.push_back(5);
	a.push_back(6);
	a.push_back(6);
	a.push_back(6);
	a.push_back(4);
	a.push_back(4);

	cout << "a.font() : " << a.front() << "\n"; 
	cout << "a.back() : " << a.back() << "\n";

	a.reverse(); // Reverse the list

	cout << "a.font() : " << a.front() << "\n"; 
	cout << "a.back() : " << a.back() << "\n";

	print_list(a);

	a.unique(); // Remove duplicate elements
	print_list(a);

	a.pop_back(); // Remove last element
	a.pop_front(); // Remove first element


	a.assign(5, 1); // 5 occurences of 1
	print_list(a);



	list<int>::iterator p;
	p = a.begin();
	advance(p, 3);
	a.insert(p,999);
	print_list(a);

	

	a.clear(); // Remove all the elements in the list

	return 0;

}

void print_list(list<int> a)
{

	list<int>::iterator p;

	p = a.begin();
	while(p != a.end())
	{
		cout << *p << "  ";
		p++;
	}
	cout << "\n";
}


/*

OUTPUT ---------

a.font() : 1
a.back() : 4
a.font() : 4
a.back() : 1
4  4  6  6  6  5  4  3  2  1
4  6  5  4  3  2  1
1  1  1  1  1
1  1  1  999  1  1

*/