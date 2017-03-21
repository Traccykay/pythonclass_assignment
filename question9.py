#Write a program that prints all the leap years in the next 100 years.
import calendar

def leap_year(year, number_of_years):
	leap_year_count = 0
	while leap_year_count < number_of_years:
		if calendar.isleap(year):
			print("{} is a leap year!".format(year))
			leap_year_count+=1
		year +=1
	leap_year(2017,100)
