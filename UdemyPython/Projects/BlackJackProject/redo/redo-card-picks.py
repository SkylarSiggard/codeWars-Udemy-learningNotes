def startinghand(dex,cards):
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

