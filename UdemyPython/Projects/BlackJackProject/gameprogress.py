
def makebet():
	choice = "Wrong"
	howmuch = 0
	while choice not in ['Y','N']:
		choice = input("\nMake a bet? (Y) for Yes (N) for No. No will default to $1 \n").upper() 
		if choice not in ['Y','N']:
			print("Sorry, You need to type Y or N \n")	
		else:
			if choice == 'Y':
				while howmuch not in ['1','2','3','4','5','6','7','8','9','10']:
					howmuch = input("\nHow much will you bet? \n")
					if howmuch not in ['1','2','3','4','5','6','7','8','9','10']:
						print("Sorry, You need to bet at least $1 \n")
				return int(howmuch)
			else:
				return 1

def fold():
	choice = "Wrong"
	while choice not in ['Y','N']:
		choice = input("\nWould you like to hit? (Y or N) \n").upper() 
		if choice not in ['Y','N']:
			print("Sorry, You need to type Y or N \n")	
	if choice == "Y":
		return True
	else:
		return False



def winners(player,hand):
	val = hand.values()
	num = 0 
	for i in val:
		num += sum(i)
	if player == 'bot':
		if num == 21:
			return False, "Bot is the winner with 21!"
		elif num > 21:
			return False, "Bot is bust"
		else:
			return True, "Keep playing"
	else:
		if num == 21:
			return False, "Player is the winner with 21!"
		elif num > 21:
			return False, "Player is bust"
		else:
			return True, "Keep playing"


