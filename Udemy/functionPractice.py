#### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
    #lesser_of_two_evens(2,4) --> 2
    #lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            print("{} is even and greater".format(a))
        else:
            print("{} is even and greater".format(b))
    elif a % 2 != 0 and b % 2 != 0:
        if a > b:
            print("{} is odd and greater".format(a))
        else:
            print("{} is odd and greater".format(b))
    else:
        if a > b:
            print("numbers are mixed but {} is greater".format(a))
        else:
            print("numbers are mixed but {} is greater".format(b))   
lesser_of_two_evens(2,4)
lesser_of_two_evens(2,5)

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter¶
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
def animal_crackers(text):
    t = text.split()
    if t[0][0] == t[1][0]:
        print(True)
    else:
        print(False)
animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False¶
#makes_twenty(20,10) --> True
#makes_twenty(12,8) --> True
#makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
    num = n1 + n2
    if n1 == 20 or n2 == 20:
        print(True, 'first')
    else:
        if num == 20:
            print(True, 'second')
        else:
            print(False, 'third')
makes_twenty(20,10)
makes_twenty(2,3)

#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name¶
#old_macdonald('macdonald') --> MacDonald
#Note: 'macdonald'.capitalize() returns 'Macdonald'
def old_macdonald(name):
    index = 0
    mystring = []
    for i in name:
        if index == 0:
            mystring.append(i.upper())
        elif index == 3:
            mystring.append(i.upper())
        else: 
            mystring.append(i)
        index = index + 1
    print(''.join(mystring))

#MASTER YODA: Given a sentence, return a sentence with the words reversed¶
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'
#Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
#
#>>> "--".join(['a','b','c'])
#>>> 'a--b--c'
#This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:
#
#>>> " ".join(['Hello','world'])
#>>> "Hello world"
