def printSeparator(title):
	print('~~~~~~~~~ ' + title + ' ~~~~~~~~~~~~~~~~')
	pass

printSeparator('Any number of arguments')
# Accepts variable number of arguments
def listStrings(*strings):
	i = 0
	#iterate through the tuple
	for s in strings:
		i += 1
		print(i, ' ', s)


listStrings('Guru', 1, 'Sarath', 'CAR', 'LOVE', 'BILLIONAIR', 'HEALTHY', 'PRIYANKA', "FAMILY", 'Business')

printSeparator('Map function')

def square(x):
	return x**2

# Using squares to create list of squares
squares = map(square, [1,2,3])
print(squares)
for s in squares:
	print(s)

printSeparator('Lambda Expressions')
f = lambda x : x*x*x
f2 = lambda x,y: x+y

print(f(3))
print(f2(3,4))

class Numbers:
	
	Nums = list()

	def __init__(self,*tupleX):
		for n in tupleX:
			self.Nums.extend([n])

	def listNums(self):
		print(self.Nums)


objNums = Numbers(1,2,3,4,5)
objNums.listNums()