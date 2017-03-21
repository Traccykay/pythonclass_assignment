#Write a python program that determines if a string is a palindrome.
a=input("Enter a String:")

def is_palindrome(a):
	ind=0
	check=True
	while ind<len(a):
		if a[ind]==a[-1-ind]:
			ind+=1
			return True
		return False
if is_palindrome(a)==True:
	print("It is a Palindrome")
else:
	print("It is not a Palindrome")
