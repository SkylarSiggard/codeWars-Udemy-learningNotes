import random
#! This is the start of game
def intro():
	print("Welcome to TikTakToe\n\n")
	
#! board game
def displayGame(board):
	print(f"\n{board[7]}|{board[8]}|{board[9]}")
	print("-+-+-")
	print(f"{board[4]}|{board[5]}|{board[6]}")
	print("-+-+-")
	print(f"{board[1]}|{board[2]}|{board[3]}\n")
	
	
	#! This is how you select the player 
def player_select():
	choice = "Wrong"
	while choice not in ["X","O"]:
		choice = input("Player 1. Please pick X or O\n").upper()
		if choice not in ["X","O"]:
			print("Sorry, I dont understand, Please pick X or O\n")
	flip = random.randint(0,1)
	if choice == "X":
		player1 = "X"
		player2 = "O"
	else:
		player1 = "O"
		player2 = "X" 
	if flip == 0:
		return 1,player1
	elif flip == 1:
		return 2,player2
	else: 
		print("something went wront") 
		
		
#! whos turn and if anyone won or not. i wanted to play it save this time
#! instead of just using X so i think this would finish better even tho its huge
def winner(t,b,p):
	if b[1] == "X" and b[2] == "X" and b[3] == "X": 
		print(f"\n\n\nPlayer {p}: {t} wins on row 1")
		return False
	elif b[4] == "X" and b[5] == "X" and b[6] == "X":
		print(f"\n\n\nPlayer {p} {t} wins on row 2")
		return False 
	elif b[7] == "X" and b[8] == "X" and b[9] == "X":
		print(f"\n\n\nPlayer {p} {t} wins on row 3")
		return False 
	elif b[1] == "X" and b[5] == "X" and b[9] == "X":
		print(f"\n\n\nPlayer {p} {t} wins on back slash")
		return False
	elif b[7] == "X" and b[5] == "X" and b[3] == "X":
		print(f"\n\n\nPlayer {p} {t} wins on forward slash")
		return False 
	elif b[1] == "O" and b[2] == "O" and b[3] == "O": 
		print(f"\n\n\nPlayer {p}: {t} wins on row 1")
		return False
	elif b[4] == "O" and b[5] == "O" and b[6] == "O":
		print(f"\n\n\nPlayer {p} {t} wins on row 2")
		return False 
	elif b[7] == "O" and b[8] == "O" and b[9] == "O":
		print(f"\n\n\nPlayer {p} {t} wins on row 3")
		return False 
	elif b[1] == "O" and b[5] == "O" and b[9] == "O":
		print(f"\n\n\nPlayer {p} {t} wins on back slash")
		return False
	elif b[7] == "O" and b[5] == "O" and b[3] == "O":
		print(f"\n\n\nPlayer {p} {t} wins on forward slash")
		return False 
	elif " " not in b:
		print(f"\n\nGame cant go on anymore. Its a tie!!")
		return False
	else:
		if ("X" or "O") not in b:
			print(f"\n\n\nMake the first Move Player {p}!")
			return True
		else:
			print("\n\n\nKeep playing")
			return True
			
#! make a move and change the player and allow the other to go 
def player_move(t,b,p):
	print(f"Player {p}'s turn ")
	game_on_bro = True
	while game_on_bro:
		turn = input("Please select one area 1 through 9\n")
		if turn not in ["1","2","3","4","5","6","7","8","9"]:
			print("Sorry please select one area 1 through 9")
		elif b[int(turn)] == "X" or b[int(turn)] == "O":	
				print("That spot has already been used") 
		else:
			b[int(turn)] = t
			if t == "X":
				t = "O"
			else:
				t = "X" 
			if p == "1":
				p = "2"
			else:
				p == "1"
			return t,b,p 
			
			
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
		
		
startGame = True
while startGame:
#! Global 
	MakingTurns = True 
	player1 = 0
	player2 = 0
	gameBoard = ["#"," "," "," "," "," "," "," "," "," "]
	#gameBoard = ["#","X","O","X","O","X","X","O","X","X"]
	intro()
	who,turn = player_select()
	if who == 1:
		player1 = 1
	else:
		player2 = 2
#! Game
#! i did the if break this time and it works so maybe that helps
	while MakingTurns:
		MakingTurns = winner(turn,gameBoard,who)
		if MakingTurns == False:
			break
		else:
			displayGame(gameBoard)
			turn,gamBoard,who = player_move(turn,gameBoard,who)
	startGame = play_again()
