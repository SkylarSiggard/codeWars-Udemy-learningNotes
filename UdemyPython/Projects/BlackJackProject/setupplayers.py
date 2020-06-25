from colorama import init 
init()
from colorama import Fore
from handlecard import start, pickcard
#? reminder how to do it :  print(Fore.RED + "some red text")
# global variables 
pot = 0  
# this is the game of blackjack. You will play against a bot. 
#! this will handle the bets 
class hits():

    def __init__(self,player,funds,first,second):
        self.player = player
        self.funds = funds
        self.first = first 
        self.second = second

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
        return Fore.WHITE + f"Player: {self.player}\nPlayer funds: {self.funds}\nCard count: "

