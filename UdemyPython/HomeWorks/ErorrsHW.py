#Handle the exception thrown by the code below by using try and except blocks.
for i in ['a','b','c']:
    try: 
        print(i**2)
    except TypeError:
        print("Hey it looks like your trying to square something other than numbers")


#Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
x = 5
y = 0
try:
    z = x/y
except:
    print("whoops something went wrong. check your variables")
finally:
    print("All Done")


#Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            square = int(input("Please put in a number to be squared"))
        except:
            print("That doesnt look like a number to me.")
        else:
            print(square**2)
            break
        #finally:
            #print("Done")  