#include <iostream>
#include <vector>

using namespace std;

int main()
{

	vector<int> v1;
	vector<int> v2(8); // Create a vector of size 8

	cout << "Size of v1 = " << v1.size() << "\n";
	cout << "Size of v2 = " << v2.size() << "\n";

	v1.push_back(5); // add elements to the end of the vector
	v1.push_back(6);
	v1.push_back(1);
	v1.push_back(10);
	v1.push_back(9);
	v1.pop_back(); // remove the last element

	cout << "Size = " << v1.size() << "\n";

	for(int i=0; i<v1.size(); i++)
	{
		cout << v1[i] << "  ";
	}
	cout << "\n";

	for(int i=0; i<v2.size(); i++)
	{
		cout << v2[i] << "  ";
	}
	cout << "\n";

	cout << "---------------------------\n";


	vector<char> v3(10,'a'); // Create a vector of size 10 and ini
	for(int i=0; i<v3.size(); i++)
	{
		cout << v3[i] << "  ";
	}
	cout << "\n";

	for(int i=0; i<v3.size() + 6; i++)
	{
		v3[i] = 'x';
	}

	for(int i=0; i<v3.size(); i++)
	{
		cout << v3[i] << "  ";
	}
	cout << "\n";


	return 0;
}


/*
OUTPUT ----------------------------

Size of v1 = 0
Size of v2 = 8
Size = 4
5  6  1  10
0  0  0  0  0  0  0  0
---------------------------
a  a  a  a  a  a  a  a  a  a
x  x  x  x  x  x  x  x  x  x

*/

