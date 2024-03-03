#birth_year = input('Birth year: ')
#age = 2024 - birth year
#print age
#will give error when ran
#cannot recognize integer minus a string
#birth year type needs to go from string to integer
#Functions that convert values into diff Types
#int() - converts to integer
#float() - converts to float
#str() - converts to string
#bool() - converts to boolean
birth_year = input('Birth Year: ')
age = 2024 - int(birth_year)
print(age)
