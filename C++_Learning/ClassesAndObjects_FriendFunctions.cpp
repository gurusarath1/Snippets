#include <iostream>

using namespace std;

/*

Friend Functions -------------

1. Friend function has access to all  private and protected members of the class which it is a friend.
2. A same function can be firend to more than one class
3. A instance function inside another class can be a friend to another class

Uses:
1. Overloading certain types of operators
2. easy I/O functions

Restrictions:
1. Friend function is not inherited by derived class.
2. cannot have storage specifier like static or extern.

*/

class Box
{

	float l,b,h; // Private by default

public:

	Box() // Constructor // Must be public
	{
		l = 0;
		b = 0;
		h = 0;
	}

	Box(float l, float b, float h) // Overloaded Constructor // Must be public
	{
		cout << "Creating Box\n";
		this->l = l;
		this->b = b;
		this->h = h;
	}

	friend float calculate_volume(Box b); // Friend function  must be declared inside the class (using friend keyword)

};


float calculate_volume(Box b) // Friend function
{
	return b.l * b.b * b.h; // Accessing the private members of the function
}

int main()
{

	Box b1(1,2,3);


	cout << calculate_volume(b1) << "\n"; // Call the friend function


	return 0;

}