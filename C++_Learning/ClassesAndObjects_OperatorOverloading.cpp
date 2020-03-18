#include <iostream>

using namespace std;

class vertex {

public:
	float x,y;

	vertex()
	{
		x = 0;
		y = 0;
	}

	vertex(float x, float y)
	{
		this->x = x;
		this->y = y;
	}

	vertex operator + (vertex &v2)
	{
		vertex v3;

		v3.x = v2.x + this->x;
		v3.y = v2.y + this->y;

		return v3;
	}
};


int main()
{

	vertex v1(3,4), v2(5,5);

	vertex v3;

	v3 = v1 + v2;

	cout << v3.x << "   " << v3.y;

	return 0;
}





