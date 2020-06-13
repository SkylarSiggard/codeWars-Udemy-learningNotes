#how to cap one letter and lower the next
def myfunc(st):
    index = 0
    mystring = []
    for i in st:
        if index % 2 == 0:
            mystring.append(st[index].lower())
        else:
            mystring.append(st[index].upper())
        index = index + 1
    return ''.join(mystring)

myfunc("hahahah")

