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

	~Box() // Destructor // Must be public
	{
		cout << "Destroying box\n";
	}

	void setDimensions(float l, float b, float h)
	{
		this->l = l;
		this->b = b;
		this->h = h;
	}

	float calculate_volume()
	{
		volume = l * b * h;
		return l * b * h;
	}

	float get_volume(); // This member function is defined outside the class (using the scope resolution operator ::)
};


float Box::get_volume()
{
	return volume;
}


int main()
{

	Box b1(1,2,3);

	cout << b1.calculate_volume() << "\n";
	b1.setDimensions(3,3,3);
	cout << b1.calculate_volume() << "\n";
	cout << b1.get_volume() << "\n";


	return 0;

}


/*
OUTPUT ------------

Creating Box
6
27
27
Destroying box

*/