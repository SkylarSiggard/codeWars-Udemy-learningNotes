from collections import Counter

mylist = [1,1,1,1,2,3,4,5,6,7,7,7,7,8,8,9]
mylist = ['a','a','a','b','b','c']

Counter(mylist)
#* return will be a dic like this {'a':3,'b':2,'c':2} or {1:4,2:1, etc }
#! you can use this will lists that are mixed data types like strings, numbers etc. 

sentence = "I want to see how many words are in this list of words so i can count all the words."
Counter(sentence.lower().split())

letters = 'aaaaaabbbbbbbbddddddccccccc'
c = Counter(letters)
c.most_common()
#! you can put a number in most_common(2) to get the two top most common 
list(c)
#* you can then make a list of the most common 





from collections import defaultdict

d = {'a':10}
#! if you were to call d['wrong key'] you would get a type error this is where defaultdict comes in to play 
d = defaultdict(lambda: 0 )
d['wrong key']




from collections import namedtuple

Dog = namedtuple("Dog",['age','breed','name'])

sammy = Dog(age=5,breed='Husky',name='Sam')
sammy.age
sammy[0]

#! this is good for large tuples that you dont know the index so you can do this so you can all the string instead of the index 