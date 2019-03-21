# Written by Guru Sarath
# Date: 31th Oct 2018

def printSeparator(title):
	print('~~~~~~~~~ ' + title + ' ~~~~~~~~~~~~~~~~')
	pass

# String
# Strings are immutable objects
printSeparator('String')
Str1 = '    This is an example string      '
Str2 = 'Hi all'
Str3 = "My Name is Guru Sarath"
Str4 = """I am the best AI/ML programmer in the world"""
Str5 = """Triple quotes allowes 
multiline strings """

print(Str1)
print(Str3)
print(Str4)
print(Str5)

#String operations
printSeparator('String operations')
print(Str1 + Str2)
print(Str3 + ', ' + Str4)
print(Str1.strip()+Str2) # Strip function removes starting and trailing blank spaces
print(Str2.replace('H', 'X'))
print(Str2.replace('all', 'M'))
print(Str2.find('X'))
print(Str2.find('a'))
print(Str4.upper())

#String iterations
printSeparator('String iterations')

for c in 'ABCDX':
	print(c)

print('A' in 'ABCD')
print('AB' in 'ABCD')
print('AC' in 'ABCD')

#Conversions 
printSeparator('Conversions')

num1 = 3.4
print(num1)
print('Num1 = ' + str(num1))
print('Num1 = ' , num1)
#print('Num1 = ' + num1) # This wont work # Cannot concatinate string and an object
decimalValue = int('3')
HexValue = int('A',16)
floatValue = float('45.68')
print(HexValue)