from colorama import init 
init()
from colorama import Fore
#? reminder how to do it :  print(Fore.RED + "some red text")

# this is the game of blackjack. You will play against a bot. 
#! this will handle the bets 
class hits():

    def __init__(self,player,funds):
        self.player = player
        self.funds = funds

    def bet(self,bet,pot):
        if self.funds == bet:
            pot = bet + pot 
            print(Fore.GREEN + "ALL IN! good luck!!")
            return pot 
        elif self.funds < bet:
            print(Fore.RED + "Not enough funds")
            return pot
        else:
            self.funds = self.funds - bet 
            pot = bet + pot
            print(Fore.GREEN + f"You made a bet if {bet}. total pot is {pot}")
            return pot 

    def __str__(self):
        return Fore.WHITE + f"Player: {self.player}\nPlayer funds: {self.funds}"

cards = {'hearts':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'spades':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'diamonds': [1,2,3,4,5,6,7,8,9,10,10,10,10,11],'clubs':[1,2,3,4,5,6,7,8,9,10,10,10,10,11]}
pot = 0 


botplayer = hits('bot',100)
botplayer.bet(20,pot)
print(botplayer)
print(Fore.BLUE + "Total pot: "+str(pot))
