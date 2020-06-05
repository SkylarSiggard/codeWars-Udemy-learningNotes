my_dictionary = {"greeting": "hello, welcome to my dictionary.", "random_numbers": [9,8,1,2,6,7,5,4,3], "random_letters": ['a', 'c', 'b'], "name": "skylar"}

#print(my_dictionary['greeting'][0:5])

if my_dictionary['greeting'][0:5] == "Hello": 
	my_dictionary['random_numbers'].reverse()
	my_dictionary['random_letters'].sort()
	print(my_dictionary.values())
elif my_dictionary['greeting'][0:5] != "Hello":
	my_dictionary.update({'greeting': "bye!"})
	print("{g} see you later {n}!".format(g = my_dictionary['greeting'], n = my_dictionary["name"]))



