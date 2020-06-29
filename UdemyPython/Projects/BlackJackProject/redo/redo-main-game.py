from colorama import init 
init()
from colorama import Fore

class hits():

    def __init__(self,player,funds,cards,dex):
        self.player = player
        self.funds = funds
        self.cards = cards 
        self.dex = dex

    def bet(self,bet,pot):
        if self.funds == bet:
            pot = bet + pot 
            print(Fore.GREEN + "ALL IN! good luck!!")
            return pot 
        elif self.funds < bet:
            print(Fore.RED + "Not enough funds")
            if self.funds >= 1:
                pot + 1
                return pot
        else:
            self.funds = self.funds - bet 
            pot = bet + pot
            print(Fore.GREEN + f"You made a bet if {bet}. total pot is {pot}")
            return pot 

    def handupdate(self,suit,card):
        self.cards[suit].append(card)


    def __str__(self):
        if self.player == "bot":
            val = self.cards.values()
            num = 0
            for i in val:
                num = sum(i) + num
            thecards = num - self.cards["hidden"][0]
        else:
            val = self.cards.values()
            num = 0
            for i in val:
                num = sum(i) + num
            thecards = num 
        return Fore.WHITE + f"Player: {self.player}\nPlayer funds: {self.funds}\nCard count: {thecards}\n"


#************************************************************************************************************

def intro():
    print(Fore.YELLOW + "\n\nWelcome to BlackJack!\n\n")

startGame = True


while startGame:
    dex = {'hearts':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'spades':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'diamonds': [1,2,3,4,5,6,7,8,9,10,10,10,10,11],'clubs':[1,2,3,4,5,6,7,8,9,10,10,10,10,11]}
    hand = {"hearts":[],"spades":[],"diamonds":[],"clubs":[],"hidden":[]}
    pot = 0
    midgame = True 
    intro()
    cards1,dex1 = startinghand(dex,hand)
    botplayer = blackjack('bot',10,cards1,dex1)
    cards2,dex2 = startinghand(dex,hand)
    realplayer = blackjack('player',20,cards2,dex2)
    print(botplayer,cards)
    print(realplayer,cards)
