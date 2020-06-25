from colorama import init 
init()
from colorama import Fore
from handlecard import start, pickcard
from players import hits

def intro():
    print(Fore.YELLOW + "\n\nWelcome to BlackJack!\n\n\n")

startGame = True


while startGame:
    dex = {'hearts':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'spades':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'diamonds': [1,2,3,4,5,6,7,8,9,10,10,10,10,11],'clubs':[1,2,3,4,5,6,7,8,9,10,10,10,10,11]}
    hand = {"hearts":[],"spades":[],"diamonds":[],"clubs":[]}
    intro()
    cards,dex = start(dex,hand)
    botplayer = hits('bot',1000,cards)
    realplayer = hits('player',1000,cards)
    #cardcount,dex = pickcard(dex)
    print(botplayer)
    print(realplayer)
    break 

#pot = botplayer.bet(20,pot)
#print(botplayer)
#print(Fore.BLUE + "Total pot: "+str(pot))