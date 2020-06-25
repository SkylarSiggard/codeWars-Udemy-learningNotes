import random
from colorama import init 
from colorama import Fore
init()
#! this is the py that will pick cards from the dex at the start and mid game.
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