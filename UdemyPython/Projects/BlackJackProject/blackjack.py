from colorama import init 
init()
from colorama import Fore
import random
#? reminder how to do it :  print(Fore.RED + "some red text")
# global variables 
pot = 0  
dex = {'hearts':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'spades':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'diamonds': [1,2,3,4,5,6,7,8,9,10,10,10,10,11],'clubs':[1,2,3,4,5,6,7,8,9,10,10,10,10,11]}
# this is the game of blackjack. You will play against a bot. 
#! this will handle the bets 
class hits():

    def __init__(self,player,funds,cardcount):
        self.player = player
        self.funds = funds
        self.cardcount = cardcount

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
        return Fore.WHITE + f"Player: {self.player}\nPlayer funds: {self.funds}\nCard count: {self.cardcount}"


def start(dex):
    s = random.randint(0,3)
    if s == 0:
        suit = "hearts"
    elif s == 1:
        suit = "spades"
    elif s == 2:
        suit = "diamonds"
    else:
        suit = "clubs"
    number = random.randint(0,len(dex[suit]))
    try:
        first = dex[suit][number]
        if suit == "hearts":
            d = random.randint(0,len(dex["spades"]))
            second = dex["spades"][d]
            del dex["spades"][d]
        else:
            d = random.randint(0,len(dex["hearts"]))
            second = dex["hearts"][d]
        del dex[suit][number]
        startingcard = first + second
        return startingcard,dex
    except:
        print(Fore.RED + "Whoops Somthing went wront at the start")

def pickcard(dex):
    s = random.randint(0,3)
    if s == 0:
        suit = "hearts"
    elif s == 1:
        suit = "spades"
    elif s == 2:
        suit = "diamonds"
    else:
        suit = "clubs"
    number = random.randint(0,len(dex[suit]))
    try:
        thecard = dex[suit][number]
        del dex[suit][number]
        return thecard, dex
    except:
        print(Fore.RED + "Whoops Somthing went wront while picking cards")


cardcount,dex = start(dex)
botplayer = hits('bot',100,cardcount)
cardcount,dex = pickcard(dex)


pot = botplayer.bet(20,pot)
print(botplayer)
print(Fore.BLUE + "Total pot: "+str(pot))
