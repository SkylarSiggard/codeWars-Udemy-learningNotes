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