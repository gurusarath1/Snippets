# Written by Guru Sarath
# Date: 19th Oct 2018


def printSeparator(title):
	print('~~~~~~~~~ ' + title + ' ~~~~~~~~~~~~~~~~')
	pass


#Sets
printSeparator("Sets")
emptySet = set()
emptyDict = {} # This is a empty dictionary # Cannot create empty dictionary this way
setNums = {1,2,3,3,4,4,5,6,7,8,9,5,5,5,5,5,5,4,4,4,4} #sets do not allow duplicates
setCars = {'Ford','BMW','VW','Honda','Toyota','Skoda'}
setAlpha = {'A','B','C'} # Sets do not have any order
setMixed = {'A','B','C', (1,2,3)}
listNums = list(setNums)
listNums2 = list({1,2,2})
tupleNums = tuple(setNums)

print(setNums)
print(setAlpha)
print(listNums)
print(listNums2)
print(setCars)

#adding element to a set 
printSeparator("Adding elements")
setX = {1,2,3}
setX.add(4) # add will add a single element
print(setX)
setX.update([0,1,2,3,4,5]) #update method can be used to add multiple elements
print(setX) 
#The update() method can take tuples, lists, strings or other sets as its argument. 
#In all cases, duplicates are avoided

#removing elements
printSeparator("removing elements")
setX.remove(0)
print(setX)
setX.discard(4)
print(setX)
setX.discard(4) 
# discard method wont throw any exception if the element is not present in the set, unlike remove method
print(setX.pop())
print(setX.pop())
print(setX.pop()) # any of the values can be poped, since sets are unordered

setX.clear()

#Operation on sets
printSeparator("Operations on sets")
A = {1,2,3,4,5,6,7,8,9}
B = {0,1,2,10,11,12,13}

print(A|B) #union A.union(B)
print(A&B) #intersection  A.intersection(B)
print(A^B) #Symmetric Difference A.symmetric_difference(B)
print(A-B) #Difference  A.difference(B)


"""
OUTPUT

~~~~~~~~~ Sets ~~~~~~~~~~~~~~~~
{1, 2, 3, 4, 5, 6, 7, 8, 9}
{'B', 'C', 'A'}
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2]
{'Honda', 'Ford', 'VW', 'Skoda', 'BMW', 'Toyota'}
~~~~~~~~~ Adding elements ~~~~~~~~~~~~~~~~
{1, 2, 3, 4}
{0, 1, 2, 3, 4, 5}
~~~~~~~~~ removing elements ~~~~~~~~~~~~~~~~
{1, 2, 3, 4, 5}
{1, 2, 3, 5}
1
2
3
~~~~~~~~~ Operations on sets ~~~~~~~~~~~~~~~~
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
{1, 2}
{0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
{3, 4, 5, 6, 7, 8, 9}
[Finished in 0.1s]

"""


"""
Python Set Methods
Method	Description
add()	Adds an element to the set
clear()	Removes all elements from the set
copy()	Returns a copy of the set
difference()	Returns the difference of two or more sets as a new set
difference_update()	Removes all elements of another set from this set
discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
intersection()	Returns the intersection of two sets as a new set
intersection_update()	Updates the set with the intersection of itself and another
isdisjoint()	Returns True if two sets have a null intersection
issubset()	Returns True if another set contains this set
issuperset()	Returns True if this set contains another set
pop()	Removes and returns an arbitary set element. Raise KeyError if the set is empty
remove()	Removes an element from the set. If the element is not a member, raise a KeyError
symmetric_difference()	Returns the symmetric difference of two sets as a new set
symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
union()	Returns the union of sets in a new set
update()	Updates the set with the union of itself and others


Built-in Functions with Set
Function	Description
all()	Return True if all elements of the set are true (or if the set is empty).
any()	Return True if any element of the set is true. If the set is empty, return False.
enumerate()	Return an enumerate object. It contains the index and value of all the items of set as a pair.
len()	Return the length (the number of items) in the set.
max()	Return the largest item in the set.
min()	Return the smallest item in the set.
sorted()	Return a new sorted list from elements in the set(does not sort the set itself).
sum()	Retrun the sum of all elements in the set.
"""