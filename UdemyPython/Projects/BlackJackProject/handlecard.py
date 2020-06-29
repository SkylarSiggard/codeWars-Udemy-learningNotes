import random
from colorama import init 
from colorama import Fore
init()
#! this is the py that will pick cards from the dex at the start and mid game.
def start1(dex,cards):
    s = random.randint(0,3)
    if s == 0:
        suit = "hearts"
    elif s == 1:
        suit = "spades"
    elif s == 2:
        suit = "diamonds"
    else:
        suit = "clubs"
    try:
        number = random.randint(0,len(dex[suit])-1)
        cards[suit].append(dex[suit][number])
        del dex[suit][number]
        cards["hidden"].append(dex["hearts"][number])
        del dex[suit][number]
        return cards, dex
    except:
        print(Fore.RED + "Whoops Somthing went wront at the start")

def start2(dex,cards):
    s = random.randint(0,3)
    if s == 0:
        suit = "hearts"
    elif s == 1:
        suit = "spades"
    elif s == 2:
        suit = "diamonds"
    else:
        suit = "clubs"
    try:
        number = random.randint(0,len(dex[suit])-1)
        cards[suit].append(dex[suit][number])
        del dex[suit][number]
        cards["hidden"].append(dex["hearts"][number])
        del dex[suit][number]
        return cards, dex
    except:
        print(Fore.RED + "Whoops Somthing went wront at the start")

def pickcard(dex):
    s = random.randint(0,3)
    if s == 0:
        suit = "clubs"
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
        return suit ,thecard, dex
    except:
        print(Fore.RED + "Whoops Somthing went wront while picking cards")