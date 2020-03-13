#include <iostream>


using namespace std;

int main()
{

	string s1("This is a string");
	string s2("Guru Sarath");
	string s4;

	s4 = "Doggy";
	string s5 = "Doggy";

	if(s4 == s5)
	{
		cout << "s4 and s5 They are equal\n";
	}

	string s3;

	s3 = s1 + s2; // Concatination

	cout << s1 << "\n";
	cout << s3 << "\n";
	cout << s1[1] << "\n"; // Access the second character

	cout << "----------------------------\n";

	string nameA = "Guru ";
	string nameB = "Nandan";
	string name = "Guru Thangamani";
	string name2 = "Sarath ";
	string name3 = "Aruna Guru Nandan";
	string name4 = "Devi";

	string nameAB = nameA + nameB;
	cout << nameAB << "\n";


	name.insert(5, name2); // insert at index 5
	cout << name << "\n";

	name3.replace(6, 11, name4); //replace(start index, length)
	cout << name3 << "\n";

	name2.erase(1, 3); // erase elements from index 1, 3 characters; erase(start index, length)
	cout << name2 << "\n";

	cout << "----------------------------\n";

	return 0;
}

/*

OUTPUT --------------------------

s4 and s5 They are equal
This is a string
This is a stringGuru Sarath
h
----------------------------
Guru Nandan
Guru Sarath Thangamani
Aruna Devi
Sth
----------------------------

*/