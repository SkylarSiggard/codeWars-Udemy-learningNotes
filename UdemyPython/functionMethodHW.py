#Write a function that computes the volume of a sphere given its radius.
#The volume of a sphere is given as r^8 * 3.14 * 4 / 3
#!mine:
def vol(rad):
    return (rad**3) * 3.14 * 4 / 3
vol(2)


#Write a function that checks whether a number is in a given range (inclusive of high and low)
#!mine
def ran_check(num,low,high):
    if num in [i for i in range(low, high +1)]:
        return str(num) + " is in the range between " + str(low) + " and " + str(high)
ran_check(5,2,7)
#same as the other but in bool form
#!mine
def ran_bool(num,low,high):
    return num in [i for i in range(low, high +1)]
ran_bool(3,1,10)

#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
#HINT: Two string methods that might prove useful: .isupper() and .islower()
#If you feel ambitious, explore the Collections module to solve this problem!
#!mine:
def up_low(s):
    d = {'upper':0,'lower':0}
    for i in s:
        if i.isupper():
            d['upper'] += 1
        elif i.islower():
            d['lower'] += 1
        else:
            pass
    print(f'No. of Upper case characters: {d["upper"]}\nNo . of Lower case characters: {d["lower"]}')
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
#!mine:
def unique_list(lst):
    return [i for i in set(lst)]

#* Thier way 
def unique_list1(lst):
    return list(set(lst))

#* another but not a fan of this way anymore 
def unique_list2(lst):
    seen_numbers = []
    for number in lst:
        if number not in seen_numbers:
            seen_numbers.append(number)
    return seen_numbers
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
unique_list1([1,1,1,1,2,2,3,3,3,3,4,5])
unique_list2([1,1,1,1,2,2,3,3,3,3,4,5])

#Write a Python function to multiply all the numbers in a list.
#Sample List : [1, 2, 3, -4]
#Expected Output : -24
#!mine
def multiply(numbers):  
    total = 1 
    for i in numbers:
        total = i * total
    return total
multiply([1,2,3,-4])

#Write a Python function that checks whether a passed in string is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
#!mine:
def palindrome(s):
    d = s.replace(" ",'')
    return d == d[::-1]
palindrome('elleh')

#Hard:
#Write a Python function to check whether a string is pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
#Hint: Look at the string module
#!mine
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    abc = [i for i in alphabet]
    for i in str1.lower():
        for j in abc:
            if i == j:
                try:
                    abc.remove(j)
                except:
                    print("tried removed same letter")
    return len(abc) == 0
ispangram("The quick brown fox jumps over the lazy dog")

#* theirs 
import string
def ispangram1(str1, alphabet=string.ascii_lowercase):
    alphabet = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphabet
ispangram1("The quick brown fox jumps over the lazy dog")

