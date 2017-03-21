#Write a python program that asks the user for her name and age and greets her with “Hello, name, you were born in 19xx”.
name=input("Please enter your name: ")
age = int(input("How old are you?: "))
Birth_year =str(2017-age)

print("Hello, {} you were born in {}".format(name,Birth_year))