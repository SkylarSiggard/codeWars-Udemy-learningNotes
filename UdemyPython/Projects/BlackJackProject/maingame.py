from colorama import init 
init()
from colorama import Fore
from handlecard import start1, start2, pickcard
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
    cards1,dex1 = start1(dex,hand)
    botplayer = hits('bot',10,cards1,dex1)
    cards2,dex2 = start2(dex,hand)
    realplayer = hits('player',10,cards2,dex2)
    print(botplayer,cards1)
    print(realplayer,cards2)
    while midgame:
        thebet = makebet() 
        pot = hits.bet(realplayer,thebet, pot)
        print(botplayer)
        print(realplayer)
        print(Fore.GREEN + f"Pot is: {pot}")
        foldingcheck = fold()
        if foldingcheck == True:
            suit,thepic,dex2 = pickcard(dex2)
            hits.handupdate(realplayer,suit,thepic)
            print(botplayer)
            print(realplayer)
        else:
            pass
        break
    break

