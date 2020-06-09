#sort numbers
def remove_smallest(numbers):
    sortnum = numbers
    for num in sortnum:
        if num == min(sortnum):
            sortnum.remove(num)
            return sortnum
#to check if the lenth of sides can make a triangle
def is_triangle(a, b, c):
    if a > 0 and b > 0 and c > 0:
        if (a + b) > c and (b + c) > a and (c + a) > b:
            return True
        else: 
            return False 
    else:
        return False
#take in a number and make it bigger. 830921 would be 983210 
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
#and how i did it...
def descending_order(num):
    myList = ([int(x) for x in str(num)])
    theList = sorted(myList)
    reeMyList = theList[::-1]
    results = [str(i) for i in reeMyList]
    str1 = ''.join(results)
    return int(str1) 
