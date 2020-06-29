from colorama import init 
init()
from colorama import Fore
from handlecard import start, pickcard
from players import hits 
from gameprogress import makebet, fold, winners

def intro():
    print(Fore.YELLOW + "\n\nWelcome to BlackJack!\n\n")

startGame = True


while startGame:
    dex = {'hearts':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'spades':[1,2,3,4,5,6,7,8,9,10,10,10,10,11],'diamonds': [1,2,3,4,5,6,7,8,9,10,10,10,10,11],'clubs':[1,2,3,4,5,6,7,8,9,10,10,10,10,11]}
    hand = {"hearts":[],"spades":[],"diamonds":[],"clubs":[],"hidden":[]}
    midgame = True 
    pot = 0
    intro()
    cards,dex = start(dex,hand)
    botplayer = hits('bot',10,cards,dex)
    realplayer = hits('player',10,cards,dex)
    print(botplayer,cards)
    print(realplayer,cards)
    while midgame:
        thebet = makebet() 
        pot1 = hits.bet(realplayer,thebet,pot)
        pot2 = hits.bet(botplayer,thebet,pot)
        print(Fore.WHITE + ' ')
        print(botplayer.cards)
        print(realplayer.cards)
        print(Fore.GREEN + f"Pot is: {pot1+pot2}")
        foldingcheck = fold()
        if foldingcheck == True:
            suit,thepic,dex = pickcard(dex)
            hits.handupdate(realplayer,suit,thepic)
            print(Fore.WHITE + ' ')
            print(botplayer.cards)
            print(realplayer.cards)
        else:
            pass
        break
    break

