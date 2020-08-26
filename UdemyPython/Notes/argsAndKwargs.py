

def myfunc(a,b,c=0,d=0):
    #return 5% of the sum of a and b 
    #you can add more params but you will hit the limit at somepoint.
    #*args will fix that
    return sum((a,b,c,d)) * 0.05
myfunc(40,60)

def myfun(*args):
    #you dont have to do args keyword but its common practice.
    return sum(args) * 0.5
myfun(50,34,34,465)

def mystuff(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("i did not find any fruit")
mystuff(fruit='apple',veggie = 'lettuce')

def myfuncs(*args, **kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfuncs(10,20,30, food='orange',animal='dog')


