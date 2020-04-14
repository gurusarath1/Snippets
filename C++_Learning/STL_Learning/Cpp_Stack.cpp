#include <iostream>
#include <stack>

using namespace std;

int main()
{

	stack<int> stk;

	stk.push(2);
	stk.push(5);
	stk.push(7);
	stk.push(1);
	stk.push(3);
	stk.push(3);

	cout << "Size of stack: " << stk.size() << "\n";
	cout << "Top of stack: " << stk.top() << "\n";

	while(!stk.empty())
	{
		cout << "Current TOS: " << stk.top() << "   ";
		stk.pop();
	}

	return 0;
}


/*

OUTPUT -------

Size of stack: 6
Top of stack: 3
Current TOS: 3   Current TOS: 3   Current TOS: 1   Current TOS: 7   Current TOS: 5   Current TOS: 2

*/

