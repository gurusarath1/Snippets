# Written by Guru Sarath
# Date: 19th Oct 2018


def printSeparator(title):
	print('~~~~~~~~~ ' + title + ' ~~~~~~~~~~~~~~~~')
	pass

#Lists
printSeparator('Lists')
emptyList = []
emptyList2 = list()
listX = [0,1,2,3,4]
tupleX = tuple(listX) # converting list to tuple
listS = [1,'A','ABC',[1,2,3], {1,2,3}]
CarsList = ['Ford','BMW','Toyota','Honda']
array = [[1,2],[3,4]]

print(emptyList2)
print(listX)
print(tupleX)
print(listS)
print(CarsList)
print(listX*3)
print(listX*-2)
print(CarsList*2)
print(array)

# indexing
printSeparator('indexing')
print(listX[0])
print(listX[-1])
print(listX[-2])
print(array[0][0])
print(array[1])
print(array[1][0])

#slicing
printSeparator('slicing')
print(listX[:])
M = 0
N = 3
print(listX[M:N]) # From Mth element to N-1th element (0 indexing)
print(listX[2:-1])
print(listX[2:])
print(listX[:3])


#Extended slicing
printSeparator('Extended slicing')
ListEXT = list(range(9))

"""
	-9 -8 -7 -6 -5 -4 -3 -2 -1    
	 0  1  2  3  4  5  6  7  8 
	[0, 1, 2, 3, 4, 5, 6, 7, 8]

"""
print(ListEXT)
print(ListEXT[-9])
print(ListEXT[0::2]) # ListEXT[start : End (excluded) : Step]
print(ListEXT[::-1]) # This Reverses the list
print(ListEXT[2:-2])
print(ListEXT[2:-2:-1])


#adding elements
printSeparator('adding elements')
print([1,2,3] + ['A','B','C'])
listS.append('YYYY')
print(listS)
listS.append(listX) #add to the list as a single element 
print(listS)
listS.extend(listX) #add to the list as multiple elements 
print(listS)
listS.append('String')
print(listS)
listS.extend('String')
print(listS)

'''
What is the difference between the list methods append and extend?
---------------------------------------------------------------------
append adds its argument as a single element to the end of a list. The length of the list itself will increase by one.
extend iterates over its argument adding each element to the list, extending the list. The length of the list will increase by however many elements were in the iterable argument.
'''

#deleting elements
printSeparator('Deleting elements')
del listX[0:2]
print(listX)

CarsList.remove('BMW')
print(CarsList)
print(CarsList.pop())
print(CarsList.pop())
print(CarsList)
CarsList.clear()

#list comprehension
printSeparator('list comprehension')
NumsList = [1,0,5,6,9,77,6,43,2,45]
listSquares = [x*x for x in NumsList]
print(listSquares)

StringList = ['Guru', 'Sarath']
lsitStringNew = ['!' + s for s in StringList]
print(lsitStringNew) 

rows = '123'
cols = 'ABCD'

crossProduct = [c + r for c in cols for r in rows]
print(crossProduct)

# Remove vowels from a sentence
textX  = 'Apple,Orange,Mango'
vowels = 'aeiouAEIOU'
withoutVowels = [letter for letter in textX if letter not in vowels]
print(''.join(withoutVowels))

"""
OUTPUT

~~~~~~~~~ Lists ~~~~~~~~~~~~~~~~
[]
[0, 1, 2, 3, 4]
(0, 1, 2, 3, 4)
[1, 'A', 'ABC', [1, 2, 3], {1, 2, 3}]
['Ford', 'BMW', 'Toyota', 'Honda']
[0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
[]
['Ford', 'BMW', 'Toyota', 'Honda', 'Ford', 'BMW', 'Toyota', 'Honda']
[[1, 2], [3, 4]]
~~~~~~~~~ indexing ~~~~~~~~~~~~~~~~
0
4
3
1
[3, 4]
3
~~~~~~~~~ slicing ~~~~~~~~~~~~~~~~
[0, 1, 2, 3, 4]
[0, 1, 2]
[2, 3]
[2, 3, 4]
[0, 1, 2]
~~~~~~~~~ Extended slicing ~~~~~~~~~~~~~~~~
[0, 1, 2, 3, 4, 5, 6, 7, 8]
0
[0, 2, 4, 6, 8]
[8, 7, 6, 5, 4, 3, 2, 1, 0]
[2, 3, 4, 5, 6]
[]
~~~~~~~~~ adding elements ~~~~~~~~~~~~~~~~
[1, 2, 3, 'A', 'B', 'C']
[1, 'A', 'ABC', [1, 2, 3], {1, 2, 3}, 'YYYY']
[1, 'A', 'ABC', [1, 2, 3], {1, 2, 3}, 'YYYY', [0, 1, 2, 3, 4]]
[1, 'A', 'ABC', [1, 2, 3], {1, 2, 3}, 'YYYY', [0, 1, 2, 3, 4], 0, 1, 2, 3, 4]
[1, 'A', 'ABC', [1, 2, 3], {1, 2, 3}, 'YYYY', [0, 1, 2, 3, 4], 0, 1, 2, 3, 4, 'String']
[1, 'A', 'ABC', [1, 2, 3], {1, 2, 3}, 'YYYY', [0, 1, 2, 3, 4], 0, 1, 2, 3, 4, 'String', 'S', 't', 'r', 'i', 'n', 'g']
~~~~~~~~~ Deleting elements ~~~~~~~~~~~~~~~~
[2, 3, 4]
['Ford', 'Toyota', 'Honda']
Honda
Toyota
['Ford']
~~~~~~~~~ list comprehension ~~~~~~~~~~~~~~~~
[1, 0, 25, 36, 81, 5929, 36, 1849, 4, 2025]
['!Guru', '!Sarath']
['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3']
ppl,rng,Mng
[Finished in 0.1s]
"""

"""
Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list


Built-in Functions with List
Function	Description
all()	Return True if all elements of the list are true (or if the list is empty).
any()	Return True if any element of the list is true. If the list is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of list as a tuple.
len()	Return the length (the number of items) in the list.
list()	Convert an iterable (tuple, string, set, dictionary) to a list.
max()	Return the largest item in the list.
min()	Return the smallest item in the list
sorted()	Return a new sorted list (does not sort the list itself).
sum()	Return the sum of all elements in the list.
"""