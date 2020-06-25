import random
from colorama import init 
from colorama import Fore
init()
#! this is the py that will pick cards from the dex at the start and mid game.


def start(dex):
    s = random.randint(0,4)
    suit = ' '
    if s == 0:
        suit = "hearts"
    elif s == 1:
        suit = "spades"
    elif s == 2:
        suit = "diamonds"
    elif s == 3:
        suit = "clubs"
    else: 
        suit = "hearts"
    try:
        number = random.randint(0,len(dex[suit]))
        if suit == "hearts":
            d = random.randint(0,len(dex["spades"]))
            cards = {"hearts": [dex["hearts"][number]], "clubs": [dex["clubs"][d]]}
            del dex[suit][number]
            del dex["clubs"][d]
            print("fist",cards)
            return cards,dex
        else:
            number = random.randint(0,len(dex[suit]))
            d = random.randint(0,len(dex["hearts"]))
            cards = {suit: [dex[suit][number]], "hearts": [dex["hearts"][d]]}
            del dex[suit][number]
            del dex["hearts"][d]
            print("Second",cards)
            return cards,dex
    except:
        print(Fore.RED + "Whoops Somthing went wront at the start. Will go to default")
        num1 = random.randint(0,13)
        if num1 == 11:
            num2 = num2 - 5
        else:
            num2 = num1 + 1
        cards = {"diamonds": [dex["diamonds"][num1]], "spades": [dex["spades"][num2]]}
        del dex["diamonds"][num1]
        del dex["spades"][num2]
        print(Fore.YELLOW + "default",cards)
        return cards, dex 

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