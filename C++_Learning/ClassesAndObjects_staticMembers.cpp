#include <iostream>

using namespace std;


/*

Static data member -------
1. Only one copy of the data member will exist for all the objects of the class
2. Initialized to zero automatically
3. Must be explicitly defined outside the class
4. Commonly used to track the number of obejcts created

Static function member ---------
1. Can only refer to other static members
2. Do not have this pointer
3. We cannot have static and non-static versions of the same function.
4. Cannot be declared as const or volatile
5. Cannot be virtual function


*/

class employee
{

	char name[20];
	int age;
	float salary;

public:

	static int numberOfEmployees; // Static variable // This does not define the variable

	employee()
	{
		numberOfEmployees += 1;
		; // Do something
	}

	static int getNumberofEmployees() // Static function
	{
		return numberOfEmployees;
	}


};

int employee::numberOfEmployees; // only now the static member gets defined

int main()
{

	employee e1,e2,e3;


	cout << e1.getNumberofEmployees() << "\n";
	cout << e3.getNumberofEmployees() << "\n";

	e1.numberOfEmployees = 100;

	cout << e3.getNumberofEmployees() << "\n";


	return 0;
} 