#List Comprehension: Given a list [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list and makes a new list that has only the even elements of this list in it.
a=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[number for number in a if number % 2==0]

print(b)