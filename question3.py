#Write a python class that accepts two integer variables and can function as a calculator with add,subtract,divide,multiply… functions
class Calculator:

	def __init__(self, value1, value2):
		self.value1=value1
		self.value2=value2
	
	def add(a,b):
		return a+b
	
	def subtract(a,b):
		return a-b
	
	def divide(a,b):
		return a//b
	
	def multiply(a,b):
		return a*b
		print("Please choose an operation.")
		print("1.Add")
		print("2.Subtract")
		print("3.Divide")
		print("4.Multiply")
		option = input("Enter an option(1/2/3/4):")
		value1 = int(input("Enter first number: "))
		value2 = int(input("Enter second number: "))
		if option == '1':
			print(value1,"+",value2,"=", add(value1,value2))
		elif option == '2':
			print(value1,"-",value2,"=", subtract(value1,value2))
		elif option == '3':
			print(value1,"*",value2,"=", multiply(value1,value2))
		elif option == '4':
			print(value1,"//",value2,"=", divide(value1,value2))
		else:
			print("Invalid input")