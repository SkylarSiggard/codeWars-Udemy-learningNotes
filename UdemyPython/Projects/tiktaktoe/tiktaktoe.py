# tik tak toe came. this is my first try that didnt really work so i made a better one

import random 
#! welcomes the player to the game and allows them to see what game it is. 
def intro():
	print("Welcome to Tic Tak Toe!!!\n\n")
#! this just shows the game board 
def displayGame(board):
	print(f"\n\n{board[7]}|{board[8]}|{board[9]}")
	print("-+-+-")
	print(f"{board[4]}|{board[5]}|{board[6]}")
	print("-+-+-")
	print(f"{board[1]}|{board[2]}|{board[3]}\n")
#! this is how they pick the player their going to use 
def player_select():
	choice = "Wrong"
	while choice not in ["X","O"]:
		choice = input("Please pick X or O\n").upper()
		if choice not in ["X","O"]:
			print("Sorry, I dont understand, Please pick X or O\n")
	flip = random.randint(0,1)
	if flip == 0:
		return "O"
	elif flip == 1:
		return "X"
	else: 
		print("something went wront be careful")
#! This is the game logic and will track whose turn it is and their move
def player_move(gameboard, player):
	errors = 0 
	board = gameboard
	who = player
	print(f"Player {player}'s turn ")
	game_on_bro = True
	while game_on_bro:
		turn = input("Please select one area 1 through 9\n")
		if turn not in ["1","2","3","4","5","6","7","8","9"]:
			print("Sorry please select one area 1 through 9")
		else:
			if board[int(turn)] == "X" or board[int(turn)] == "O":
				errors += 1
				if errors >=3:
					print("Game is a tie")
					return False
				else:
					print("That spot has already been used")
			elif used_spots == 10:
				return False 
			else:
				board[int(turn)] = player
				if who == "X":
					who = "O"
				else:
					who = "X"
		return board,who, True 
#! this tracks the progress and checks if the game is still going. 		
def player_progress(board, player):
	global used_spots
	if board[1] == player and board[2] == player and board[3] == player: 
		print(f"\n\n\nPlayer {player} wins on row 1")
		return False
	elif board[4] == player and board[5] == player and board[6] == player:
		print(f"\n\n\nPlayer {player} wins on row 2")
		return False 
	elif board[7] == player and board[8] == player and board[9] == player:
		print(f"\n\n\nPlayer {player} wins on row 3")
		return False 
	elif board[1] == player and board[5] == player and board[9] == player:
		print(f"\n\n\nPlayer {player} wins on back slash")
		return False
	elif board[7] == player and board[5] == player and board[3] == player:
		print(f"\n\n\nPlayer {player} wins on forward slash")
		return False 
	else:
		#* THIS AREA IS STILL BROKEN SO I NEED TO GO BACK AN FIT THIS, 
		#* BUT ITS NOT THAT BIG OF A DEAL. I got it to work but its
		#* not super clean 
		for i in range(1,10):
			if board[i] == "X" or board[i] == "O":
				used_spots += 1
				if used_spots == 9:
					print("\n\n\nThe gameboard is full no winners")
					return False
				else: 
					used_spots = 0 
					print("\n\n\nKeep playing")
					return True
#! will end the game or start again. 
def play_again():
	choice = "Wrong"
	while choice not in ["Y","N"]:
		choice = input("\nKeep playing?: (Y or N)\n").upper()
		if choice not in ["Y","N"]:
			print("Sorry, I dont understand, Please choose Y or N\n")	
	if choice == "Y":	
		print("Starting new game")
		return True 
	elif choice == "N":
		print("\n\n\nGoodbye!!")
		return False		
game_turn_on = True
while game_turn_on:
	player = "Player needs to be made"
	gameboard = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
	used_spots = 0
	start = True 
	intro()
	player = player_select()
	while start: 
		displayGame(gameboard)
		gameboard,player,start = player_move(gameboard, player) 
		start = player_progress(gameboard,player)
	game_turn_on = play_again()
# track 