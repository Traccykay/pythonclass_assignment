largest=None

while True:
	my_input = input("Please Enter a number: ")
	if my_input == "done":
		break
	try:
		number = float(my_input)
	except:
		print("Invalid input")
		continue
	if largest is None or number > largest:
		largest = number
print("largest:", largest)
