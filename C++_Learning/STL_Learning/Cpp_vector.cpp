#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int find_element(vector<int>&, int K);

int main()
{
	vector<int> v1;
	vector<int> v2(8); // Create a vector of size 8

	cout << "Size of v1 = " << v1.size() << "\n";
	cout << "Size of v2 = " << v2.size() << "\n";

	v1.push_back(5); // add elements to the end of the vector
	v1.push_back(6);
	v1.push_back(1);
	v1.push_back(10);
	v1.push_back(9);
	v1.pop_back(); // remove the last element

	cout << "Size = " << v1.size() << "\n";

	for(int i=0; i<v1.size(); i++) {
		cout << v1[i] << "  ";
	}
	cout << "\n";

	for(int i=0; i<v2.size(); i++) {
		cout << v2[i] << "  ";
	}
	cout << "\n";

	cout << "---------------------------\n";


	vector<char> v3(10, 'a'); // Create a vector of size 10 and initialize to 'a'
	for(int i=0; i<v3.size(); i++) {
		cout << v3[i] << "  ";
	}
	cout << "\n";

	for(int i=0; i<v3.size() + 6; i++) {
		v3[i] = 'x';
	}

	for(int i=0; i<v3.size(); i++) {
		cout << v3[i] << "  ";
	}
	cout << "\n";


	cout << "---------------------------\n";

	vector<float> a;
	vector<float> b;

	a.push_back(9.1);
	a.push_back(1.5);
	a.push_back(0.5);

	b.push_back(10.1);
	b.push_back(6.5);
	a.push_back(7.5);

	if(a == b) {
		cout << "a and b vector are equal \n";
	} else {
		cout << "a and b Not Equal\n";
	}

	vector<float> c;

	if(c.empty()) {
		cout << "c vector is empty\n";
	}

	cout << "====================== Find an element in vector ======================\n";

	vector<int> testing = {1,2,4,4,7,8,9,10,13,16,24,67};
	cout << "7 is at index = " << find_element(testing, 7) << endl;

	cout << "====================== Sorting ======================\n";

	vector<int> unsorted_vector = {3,54,2,34,63,72,57,27,45,1,85,90,0,55,5,33,28,3};
	sort(unsorted_vector.begin(), unsorted_vector.end());
	for(auto i : unsorted_vector) {
		cout << i << "  ";
	}
	cout << endl;

	cout << "====================== Reversing ======================\n";

	reverse(unsorted_vector.begin(), unsorted_vector.end());
	for(auto i : unsorted_vector) {
		cout << i << "  ";
	}
	cout << endl;

	cout << "====================== Min / Max ======================\n";

	cout << "Min = " << min(3,4) << endl;
	cout << "Max = " << max(9,11) << endl;
	cout << "Max = " << max('a','c') << endl;

	vector<int> vecA = {3,2,1,4,5,6};

	auto  it_obj = min_element(vecA.begin(), vecA.end());
	cout << "Min in vecA = " << distance(vecA.begin(), it_obj) << endl;

	it_obj = max_element(vecA.begin(), vecA.end());
	cout << "Max in vecA = " << distance(vecA.begin(), it_obj) << endl;

	cout << "====================== Removing ======================\n";

	remove(vecA.begin(), vecA.end(), 4);
	for(auto i : vecA) {
		cout << i << "  ";
	}
	cout << endl;

	remove(vecA.begin(), vecA.end(), 6);
	for(auto i : vecA) {
		cout << i << "  ";
	}
	cout << endl;

	remove(vecA.begin(), vecA.end(), 3);
	for(auto i : vecA) {
		cout << i << "  ";
	}
	cout << endl;

	cout << "====================== Delete all elements (clear) ======================\n";

	vecA.clear();

	cout << "====================== assign ======================\n";

	// Assigns new contents to the vector, replacing its current contents, and modifying its size accordingly.

	vecA.assign(5, 999); // assign(num_elements, value)
	for(auto i : vecA) {
		cout << i << "  ";
	}
	cout << endl;

	vecA.assign(3, 111); // assign(num_elements, value)
	for(auto i : vecA) {
		cout << i << "  ";
	}
	cout << endl;

	return 0;
}


int find_element(vector<int>& vec, int K) {
	auto iter_obj = find(vec.begin(), vec.end(), K);

	if(iter_obj != vec.end()) {
		return distance(vec.begin(), iter_obj);
	} else {
		return -1;
	}
}


/*
OUTPUT ----------------------------

Size of v1 = 0
Size of v2 = 8
Size = 4
5  6  1  10
0  0  0  0  0  0  0  0
---------------------------
a  a  a  a  a  a  a  a  a  a
x  x  x  x  x  x  x  x  x  x
---------------------------
a and b Not Equal
c vector is empty

*/





/*
Size of v1 = 0
Size of v2 = 8
Size = 4
5  6  1  10
0  0  0  0  0  0  0  0
---------------------------
a  a  a  a  a  a  a  a  a  a
x  x  x  x  x  x  x  x  x  x
---------------------------
a and b Not Equal
c vector is empty
====================== Find an element in vector ======================
7 is at index = 4
====================== Sorting ======================
0  1  2  3  3  5  27  28  33  34  45  54  55  57  63  72  85  90
====================== Reversing ======================
90  85  72  63  57  55  54  45  34  33  28  27  5  3  3  2  1  0
====================== Min / Max ======================
Min = 3
Max = 11
Max = c
Min in vecA = 2
Max in vecA = 5
====================== Removing ======================
3  2  1  5  6  6
3  2  1  5  6  6
2  1  5  6  6  6
====================== Delete all elements (clear) ======================
====================== assign ======================
999  999  999  999  999
111  111  111
*/
