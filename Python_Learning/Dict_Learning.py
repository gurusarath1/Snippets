# Written by Guru Sarath
# Date: 20th Oct 2018


def printSeparator(title):
	print('~~~~~~~~~ ' + title + ' ~~~~~~~~~~~~~~~~')
	pass


#Dictionary
printSeparator("Dictionary")
emptyDictionary = {}
dict1 = {'A':1, 'B':2, 'C':3}
dict2 = {'A':1, 9:'Nine', (2,3):'Nums', 'Hi':'All'} 
#key of a dictionary has to be an immutable object like - string, tuple etc
dict3 = dict([('A',999),('B',111),('C',666)])

print(dict1)
print(dict2)
print(dict3)



#indexing
printSeparator("indexing")
print(dict1['B'])
print(dict2[9])
print(dict2[(2,3)])
print(dict3['A'])

print(dict1.get('B')) 
#get method will return none if the key does not exist
#get method wont throw a key error


#Updating
printSeparator("Updating")
print(dict1)
dict1['A'] = 1000
print(dict1)
dict1['B'] = 'Guru Sarath'
print(dict1)
dict1['D'] = "New Guy" #adding an element to dict
print(dict1)

#membership test
printSeparator("Test")
# We can test if a key is in a dictionary or not using the keyword in. 
# Notice that membership test is for keys only, not for values.
print('A' in dict1)
print('X' in dict1)


#Iteration 
printSeparator("dictionary iteration")
dict1X = {'A':1, 'B':2, 'C':3}

# Iteration loops through the keys of the dictionary
for keyX in dict1X:
	print(keyX, ' - ', dict1X[keyX])


#dictionary comprehension
printSeparator("dictionary comprehension")
squaresLoopUp = {x : x**2 for x in range(9)}
print(squaresLoopUp)

# Creating dictionary from two lists (one to one mapping)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = range(26)
dictA_numMap = {letter:number for letter,number in zip(letters,numbers)}
print(dictA_numMap)

#Reversing keys and values of a dictionary
dictX = {'CAR':1, 'BIKE':2, 'CYCLE':3}
dixt_reverse_X = {dictX[key] : key  for key in dictX}
print(dixt_reverse_X)




"""
OUTPUT
~~~~~~~~~ Dictionary ~~~~~~~~~~~~~~~~
{'A': 1, 'B': 2, 'C': 3}
{'A': 1, 9: 'Nine', (2, 3): 'Nums', 'Hi': 'All'}
{'A': 999, 'B': 111, 'C': 666}
~~~~~~~~~ indexing ~~~~~~~~~~~~~~~~
2
Nine
Nums
999
2
~~~~~~~~~ Updating ~~~~~~~~~~~~~~~~
{'A': 1, 'B': 2, 'C': 3}
{'A': 1000, 'B': 2, 'C': 3}
{'A': 1000, 'B': 'Guru Sarath', 'C': 3}
{'A': 1000, 'B': 'Guru Sarath', 'C': 3, 'D': 'New Guy'}
~~~~~~~~~ Test ~~~~~~~~~~~~~~~~
True
False
~~~~~~~~~ dictionary iteration ~~~~~~~~~~~~~~~~
A  -  1
B  -  2
C  -  3
~~~~~~~~~ dictionary comprehension ~~~~~~~~~~~~~~~~
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
{'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
{1: 'CAR', 2: 'BIKE', 3: 'CYCLE'}
[Finished in 0.1s]
"""


"""
Python Dictionary Methods
Method	Description
clear()	Remove all items form the dictionary.
copy()	Return a shallow copy of the dictionary.
fromkeys(seq[, v])	Return a new dictionary with keys from seq and value equal to v (defaults to None).
get(key[,d])	Return the value of key. If key doesnot exit, return d (defaults to None).
items()	Return a new view of the dictionary's items (key, value).
keys()	Return a new view of the dictionary's keys.
pop(key[,d])	Remove the item with key and return its value or d if key is not found. If d is not provided and key is not found, raises KeyError.
popitem()	Remove and return an arbitary item (key, value). Raises KeyError if the dictionary is empty.
setdefault(key[,d])	If key is in the dictionary, return its value. If not, insert key with a value of d and return d (defaults to None).
update([other])	Update the dictionary with the key/value pairs from other, overwriting existing keys.
values()	Return a new view of the dictionary's values


Built-in Functions with Dictionary
Function	Description
all()	Return True if all keys of the dictionary are true (or if the dictionary is empty).
any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
len()	Return the length (the number of items) in the dictionary.
cmp()	Compares items of two dictionaries.
sorted()	Return a new sorted list of keys in the dictionary.
"""