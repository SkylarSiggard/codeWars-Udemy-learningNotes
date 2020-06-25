
def makebet():
	choice = "Wrong"
	while choice not in ['1','2','3','4','5','6','7','8','9','10']:
		choice = input("\nMake a bet? \n")
		if choice not in [1,2,3,4,5,6,7,8,9,10]:
			print("Sorry, You need to bet at least $1 \n")	
	return int(choice)

