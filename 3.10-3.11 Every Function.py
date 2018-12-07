countries = ['pakistan', 'china', 'indonesia', 'europe', 'india']
print(countries)
print("\nLength of list")
print(len(countries))
print("Reversed countries: ")
countries.reverse()
print(countries)
print("Sorting Alphabetically: ")
print(sorted(countries))
print("Removing India from the list by value")
countries.remove('india')
print(countries)
print("Removing element by using del statement :")
del countries[2]
print(countries)
print("Printing the first element of list: ")
print(countries[0].title())
print("I am from " + countries[0])
print("Inserting Belgium in list")
countries.insert(2, 'Belgium')
print(countries)
print("Getting index error intenionally: ")
print(countries[6])







