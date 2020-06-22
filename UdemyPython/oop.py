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


#* here is another example of a class: 
class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius 
        self.area = radius*radius*Circle.pi
    def get_circunference(self):
        return self.radius*Circle.pi*2
    
    
#! Polymorphism 
class PolyDog():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " say woof!"
#! Polymorphism 
class PolyCat():
    def __init__(self,name):
        self.name = name
    def speak(self):
        return self.name + " say meow!"
niko = PolyDog("niko")
felix = PolyCat("felix")
print(niko.speak())

#! for loop example 
for pet  in [niko,felix]:
    print(type(pet))
    print(pet.speak())

#! making a function examle: 
def pet_speak(pet):
    print(pet.speak())
    
#! good example of what you can do with it and first time seeing an raise error 
class AnimalNew():
    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass must implement this adstract methond")
    
class PolyDogNew(AnimalNew):
    def speak(self):
        return self.name + " says woof !!!"
    
#* *********************************************************************************************************************
#! Special Methods (magic/Dunder)
class Book():
    def __init__(self,title,author,pages,):
        self.title = title
        self.author = author
        self.pages = pages
    #* this is used if you ever want to put something in print()
    def __str__(self):
        return f"{self.title} by {self.author}"
    #* this is used if you want to see the len() 
    def __len__(self):
        return self.pages
    #* this will be used if someone used the del to delete soemthing 
    def __del__(self):
        print("A book object has been deleted")

b = Book("Python","Jose",200)

#! this wouldnt normal work without having the magic methonds in that Book class
print(b)
len(b)

#! will delete the book or item from memory 
del b 

