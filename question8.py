#Write a python program that asks the user for a number n and prints the sum of all the numbers between 1 and n

m = int(input("Please Enter a number: "))
sum = 0

for i in range (1,m+1):
    sum += i
    print(i)
print(sum)