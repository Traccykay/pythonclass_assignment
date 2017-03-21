#Write a python program that asks the user for a number n and prints the sum of all the numbers between 1 and n
number = 50

number = int(input("Enter a number: "))
sum=0

while(number>0):
	sum += number
	number -=1

	print("The sum is", sum)