#include <iostream>
#include <queue>

using namespace std;

int main()
{

	priority_queue<int> PQ; // MAX heap
	// priority_queue<int>::iterator i;  // No iterator

	PQ.push(2);
	PQ.push(8);
	PQ.push(1);
	PQ.push(7);

	cout << "Size = " << PQ.size() << "\n";
	cout << "Top element = " << PQ.top() << "\n";

	while(!PQ.empty())
	{
		cout << "Top : " << PQ.top() << "  ";
		PQ.pop();
	}


	return 0;
}

/*

OUTPUT - 

Size = 4
Top element = 8
Top : 8  Top : 7  Top : 2  Top : 1


*/