# Written by Guru Sarath
# Date: 19th Oct 2018


"""
What is tuple?
In Python programming, a tuple is similar to a list. 
The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas in a list, elements can be changed.

Advantages of Tuple over List
Since, tuples are quite similiar to lists, both of them are used in similar situations as well.

However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

We generally use tuple for heterogeneous (different) datatypes and list for homogeneous (similar) datatypes.
Since tuple are immutable, iterating through tuple is faster than with list. So there is a slight performance boost.
Tuples that contain immutable elements can be used as key for a dictionary. With list, this is not possible.
If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

"""

def printSeparator(title):
	print('~~~~~~~~~ ' + title + ' ~~~~~~~~~~~~~~~~')
	pass


# Tuple
emptyTuple = ()
emptyTuple2 = tuple()
TupleX = (1,2,3)

print(TupleX)

ListX = list(TupleX)

print(ListX)



"""
Python Tuple Method
Method	Description
count(x)	Return the number of items that is equal to x
index(x)	Return index of first item that is equal to x


Built-in Functions with Tuple
Function	Description
all()	Return True if all elements of the tuple are true (or if the tuple is empty).
any()	Return True if any element of the tuple is true. If the tuple is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of tuple as pairs.
len()	Return the length (the number of items) in the tuple.
max()	Return the largest item in the tuple.
min()	Return the smallest item in the tuple
sorted()	Take elements in the tuple and return a new sorted list (does not sort the tuple itself).
sum()	Retrun the sum of all elements in the tuple.
tuple()	Convert an iterable (list, string, set, dictionary) to a tuple.

"""