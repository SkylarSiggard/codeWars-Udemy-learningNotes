
def hello1(name='Jose'):
    print("the hello() funtion has been executed!")
    
    def greet():
        return '\n This is the greet() func inside hello'
    
    def welcome():
        return '\n this is welcome() in func'
    
    
    if name == 'Jose':
        return greet
    else:
        return welcome
    #print(greet())
    #print(welcome())
    #print("this is the end of the func")

my_new_func = hello1("Jose")

print(my_new_func())

def cool():
    
    def super_cool():
        return "I am cool"
    
    return super_cool

some_func = cool()

some_func() 





def hello():
    return "hello skylar"

def other(some_other_func):
    print("other code runs here!")
    print(some_other_func())

other(hello)





def new_decorator(original_func):
    def wrap_func():
        
        print('some extra code')
        
        original_func()
        
        print("some extra code after the original func")
    
    return wrap_func 



@new_decorator
def func_needs_dec():
    print("i want to be decorated")

decorated_func = new_decorator(func_needs_dec)

decorated_func()


