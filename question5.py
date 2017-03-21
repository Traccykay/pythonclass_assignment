#Write a python function that accepts a list of words then prints them sorted in alphabetical order.
def sort_list():
	list = input("Enter a list of words: ")
	 words = list.split()
	 words.sort()
	 print("The sorted words are: ")
	 for word in words:
	 	print(word)