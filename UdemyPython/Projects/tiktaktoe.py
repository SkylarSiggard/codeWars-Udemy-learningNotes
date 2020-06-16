#! welcomes the player to the game and allows them to see what game it is. 
def intro():
	print("Welcome to Tic Tak Toe!!!")
#! this just shows the game board 
def displayGame(board):
	print(f"{board[7]}|{board[8]}|{board[9]}")
	print("-+-+-")
	print(f"{board[4]}|{board[5]}|{board[6]}")
	print("-+-+-")
	print(f"{board[1]}|{board[2]}|{board[3]}")
#! this is how they pick the player their going to use 
def player_select():
	choice = "Wrong"
	while choice not in ["X","O"]:
		choice = input("Please pick X or O. ").upper()
		if choice not in ["X","O"]:
			print("Sorry, I dont understand, Please pick X or O")
	if choice == "X":
		return choice
	elif choice == "O":
		return choice
	else: 
		print("something went wront be careful")
#! This is the game logic and will track whose turn it is and their move
def player_move(gameboard, player):
	board = gameboard
	who = player
	print(f"Player {player}'s turn ")
	game_on_bro = True
	while game_on_bro:
		turn = input("Please select one area 1 through 9.  ")
		if turn not in ["1","2","3","4","5","6","7","8","9"]:
			print("Sorry please select one area 1 through 9")
		else:
			if board[int(turn)] == "X" or board[int(turn)] == "O":
				print("That spot has already been used")
			else:
				board[int(turn)] = player
				if who == "X":
					who = "O"
				else:
					who = "X"
		return board,who 
#! this tracks the progress and checks if the game is still going. 		
def player_progress(board, player):
	if board[1] == player and board[2] == player and board[3] == player: 
		print(f"Player {player} wins on row 1")
		return False
	elif board[4] == player and board[5] == player and board[6] == player:
		print(f"Player {player} wins on row 2")
		return False 
	elif board[7] == player and board[8] == player and board[9] == player:
		print(f"Player {player} wins on row 3")
		return False 
	elif board[1] == player and board[5] == player and board[9] == player:
		print(f"Player {player} wins on back slash")
		return False
	elif board[7] == player and board[5] == player and board[3] == player:
		print(f"Player {player} wins on forward slash")
		return False 
	else:
		print("Keep playing")
		return True
#! will end the game or start again. 
def play_again():
	choice = "Wrong"
	while choice not in ["Y","N"]:
		choice = input("Keep playing?: (Y or N)").upper()
		if choice not in ["Y","N"]:
			print("Sorry, I dont understand, Please choose Y or N")	
	if choice == "Y":	
		print("Starting new game")
		return True 
	elif choice == "N":
		print("Goodbye!!")
		return False		
game_turn_on = True
while game_turn_on:
	player = "Player needs to be made"
	gameboard = {1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}
	start = True 
	player = player_select()
	while start: 
		displayGame(gameboard)
		gameboard,player = player_move(gameboard, player) 
		start = player_progress(gameboard,player)
	game_turn_on = play_again()
