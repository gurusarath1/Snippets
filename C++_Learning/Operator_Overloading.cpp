#include <iostream>

/*

retrun-type operator# (arg-lsit)
{
	// Operation
}

*/
/*

Restrictions -----
1. You cannot change the precedence
2. Cannot change the number of operands (Expect for function call operator)
3. operator funcitons cannot have default arguments
4. These Operators cannot be overloaded . :: .* ?
5. Some operators cannot be overloaded with friend functions [] () ->
All operator functions are inherited except = operator


*/


using namespace std;

class vertex
{

public:

	float x, y;

	vertex(float x, float y)
	{
		this->x = x;
		this->y = y;
	}

	vertex()
	{
		x = 0;
		y = 0;
	}

	vertex operator+(vertex& right_operand)
	{
		return vertex(this->x + right_operand.x, this->y + right_operand.y);
	}

	vertex operator-(vertex& right_operand)
	{
		return vertex(this->x - right_operand.x, this->y - right_operand.y);
	}

	// Prefix increment
	vertex operator++()
	{
		this->x++;
		this->y++;

		return *this;
	}

	// Postfix increment	
	vertex operator++(int x)
	{
		this->x++;
		this->y++;

		return *this;
	}

	// To use [] operator on right side
	float operator[](int index)
	{
		if (index == 0)
			return this->x;
		else
			return this->y;
	}

	vertex operator()(float x, float y)
	{
		this->x = x;
		this->y = y;

		return *this;
	}



	friend ostream& operator<<(ostream& os, vertex& v);
	friend vertex operator+(float first_operand, vertex& second_operand);
	friend vertex operator+(vertex& first_operand, float second_operand);

};

ostream& operator<<(ostream& os, vertex& v)
{
	os << "( " << v.x << " , " << v.y << " )";
	return os;
}

vertex operator+(float first_operand, vertex& second_operand)
{
	vertex v3;
	v3.x = first_operand + second_operand.x;
	v3.y = first_operand + second_operand.y;

	return v3;
}

vertex operator+(vertex& first_operand, float second_operand)
{
	vertex v3;
	v3.x = first_operand.x + second_operand;
	v3.y = first_operand.y + second_operand;

	return v3;
}


int main()
{

	vertex v1(3, 2);
	vertex v2(4, 1);

	vertex v3 = 5 + v1 + v2;
	vertex v4 = v1 - v2;

	cout << "\nv3[1] = " << v3[1];
	cout << "\nv3 = " << v3;
	cout << "\nv4 = " << v4;

	v3++;
	++v3;

	v4 = v4 + 9;

	cout << "\nv3 = " << v3;


	return 0;
}