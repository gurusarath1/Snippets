# Written by Guru Sarath
# 17 - Nov - 2018

# -----------------------------------------
def Disp(prefix):

	def displayMessage(message):
		print(prefix + ": " + message)

	return displayMessage


MessageType1 = Disp('Cation')
MessageType1('Wet Floor')
# -----------------------------------------

def decoratorFunction(functionX):

	def WrapperFunction():
		print('Wrapper Starts -- ')
		functionX()
		print('Wrapper Ends -- ')

	return WrapperFunction


def funcX():
	print('This FuncX')

X = decoratorFunction(funcX)
X()

# -----------------------------------------

def decoratorFunction_2(functionX):

	def WrapperFunction():
		print('Wrapper Starts -- ')
		functionX()
		print('Wrapper Ends -- ')

	return WrapperFunction

@decoratorFunction_2
def funcX_2():
	print('This FuncX_2')

funcX_2()

# -----------------------------------------
