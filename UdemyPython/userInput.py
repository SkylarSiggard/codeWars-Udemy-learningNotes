
result = input('please put in a value: ')
print(int(result))
#This is the way to add a user in put then assigning it to something. Later we can use that input for a function or some other thing to have that input actually do
#something we want it to do. All inputs will return a string so its important to use float(), int() or something to make that input the data type you want so you can 
#use it how you would like. 
#
#You use a while loop to make sure your getting back the input or close to the input you would want. 

#! if you want a input to be a number this is a way of many different ways of doing it. 

def user_choice():
    choice = "Wrong"
    
    while choice.isdigit() == False:
        
        choice = input("Please enter a number (0-20): ")
        
        if choice.isdigit() == False:
            print("Sorry that is not a digit!")
    
    return int(choice)


#* you can also us a list of acceptable inputs. example:
results = 'WRONG Value'
acceptable_values = [1,2,3]
results in acceptable_values
results not in acceptable_values


#* this is how it can be used:
def user_choice1():
    #!setup 
    choice = "Wrong"
    acceptable_range = range(0,10)
    within_range = False
    #! digit check 
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-9): ")
    #range check 
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("sorry you out of range. needs to be 1-9")
                within_range = False
        else:
            print('sorry it needs to be a number')
    
    return int(choice)

