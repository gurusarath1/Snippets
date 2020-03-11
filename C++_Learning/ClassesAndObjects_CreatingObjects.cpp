#include <iostream>

using namespace std;

class Box
{

	float l,b,h, volume; // Private by default

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

	float calculate_volume()
	{
		volume = l * b * h;
		return l * b * h;
	}

};



class sphere
{
	float volume, r;

public:
	sphere(float r)
	{
		cout << "Creating Sphere\n";
		this->r = r;
	}
};


int main()
{
	Box b1(1,2,3); // Way to create object 1
	Box b2 = Box(2,2,4); // Way to create object 2
	sphere s1(3);
	sphere s2 = 4; // Way to create obejct 3 (only works for objects with constructors with one parameter)

	return 0;
}

/*
OUTPUT --------

Creating Box
Creating Box
Creating Sphere
Creating Sphere

*/