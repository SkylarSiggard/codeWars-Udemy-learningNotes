def square(num):
    return num**2
my_nums = [1,2,3,4,5]
#for loop way to return each item in the list after the function 
for item in map(square, my_nums):
    print(item)
#make a list with the outputs of the funciton 
list(map(square, my_nums))

#more examples:
def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['Andy','Eve','Sally']
list(map(splicer,names))

#! FILTER:
# will return a bool. 
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
# make a list of all the items that are true from the function 
list(filter(check_even,mynums))
# return each item that returns true:
for n in filter(check_even,mynums):
    print(n)


#! LAMBDA
# breaking down a regular function down to a lambda:
def squre(num):
    result = num ** 2
    return result
#or 
def square2(num): return num ** 2
#make a lamb. i added the number at the end of the funtion because i didnt want broke code. 
lambda num: num ** 2
#lamb name. i added the number at the end of the funtion because i didnt want broke code. 
square2 = lambda num: num ** 2

# how to use them in a map:
list(map(lambda num:num**2,mynums))
# how to use them in a filter:
list(filter(lambda num:num%2 == 0, mynums))

