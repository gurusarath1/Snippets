#include <iostream>

using namespace std;

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

	float get_volume()
	{
		return l * b * h;
	}


};

int main()
{

	Box b1(1,2,3);

	cout << b1.get_volume() << "\n";

	b1.setDimensions(3,3,3);

	cout << b1.get_volume() << "\n";


	return 0;

}