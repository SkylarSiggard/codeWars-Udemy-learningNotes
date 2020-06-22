oop = "Object Oriented Programming"
#!  class NameOfClass():
#!     def__init__(self,param1,param2):
#!       self.param1 = param1
#!       self.param2 = param2
#!     def some_method(self):
#*        preform some action 
#!        print(self.param1)

class SampleWord():
    #notice it is camelcase. that way of typing should be saved for classes,
    pass 
my_sample = SampleWord()
print(type(my_sample))
#! output is __main__.Sample
#* this main is showing that we're in the main area. 

class Dog():
    def __init__(self,breed):
        self.breed = breed 

my_dog = Dog(breed="GoldenDoodle")
print(my_dog.breed) #! output is "GoldenDoodle"

class DogExample2():
    
    # class object attrubute 
    # same for any insteance of a class 
    species = 'mammal'
    
    
    def __init__(self,breed,name,spots):
        # attibutes 
        # we take in the argument 
        # assign it using self.attruibute_name
        self.name = name
        self.breed = breed 
        
        # expect boolean True/False 
        self.spots = spots 
    # operation/ actions ---> Methods 
    def bark(self):
        print("WOOF! My name is {}".format(self.name))
my_dog = DogExample2(breed="GoldenDoodle", name="Skilo", spots=False)
my_dog.bark()
#! Methods are different then the others because we have to invoke them with () 

