from operator import itemgetter, attrgetter
import operator 

# global vars 
similarities = {}

#Read in booklist
with open("booklist.txt", 'r') as f:
    pass
    books = []
    for line in f:
        books.append(tuple(line.strip().split(',')))

#Read in Ratings
with open("ratings.txt", 'r') as f:
    ratings = {}
    while True:
        name = f.readline().strip().lower()
        if not name:
            break
        scores = f.readline().strip().split()
        ratings[name] = [int(score) for score in scores]

def dotprod(x, y):
    assert len(x) == len(y)
    return sum(x[i]*y[i] for i in range(len(x)))


def compute_scores():
    for name1 in ratings:
        for name2 in ratings:
            if name1 != name2:
                affinityScore = dotprod(ratings[name1], ratings[name2])
                if affinityScore > 0:
                    similarities[name1] = similarities.get(name1, {})
                    similarities[name1][name2] = affinityScore


def friends(name):
    affinityScores = similarities[name]
    return affinityScores

# will sort the top 3 and return them as a tuple. 
def sortme(s):
    allcommons = {}
    for i in s:
        x = sorted(similarities[i].items(), key=operator.itemgetter(1), reverse=True)
        allcommons[i] = x[0] , x[1] , x[2]
    return allcommons
# if you wanted an imput a name to check common likers 
def findmecommon(s):
    readers = []
    choice = 'wrong'
    for i in s:
        readers.append(i)
    while choice not in readers:
        choice = input("Please input a name of a reader  ").lower()
        if choice not in readers:
            print("Sorry, but I cant find that reader. Try again! ")
    x = sorted(similarities[choice].items(), key=operator.itemgetter(1), reverse=True)
    return choice , x[0] , x[1] , x[2]
# now i need to find the top rated books for both common readers 
# then compare the rates 5 or 0 if its a zero then i bet they reader has already read it and dont need the recommend 
def recommendfinder(person):
    index = 0
    reader1 = []
    reader2 = []
    readthese = []
# the person you searching for's top reviewed books 
    for i in ratings[person[0]]:
        if i >= 4:
            reader1.append(books[index])
            index = 1 + index
        else:
            index = 1 + index
    index = 0
# find the first common persons top reviewed books 
    for i in ratings[person[1][0]]:
        if i >= 4:
            reader2.append(books[index])
            index = 1 + index
        else:
            index = 1 + index 
    index = 0
# find the second common persons top reviewed books 
    for i in ratings[person[2][0]]:
        if i >= 4:
            reader2.append(books[index])
            index = 1 + index
        else:
            index = 1 + index
    for i in reader2:
        if i not in reader1:
            readthese.append(i)
        else:
            pass 
    return readthese


# run main 
def main():
    compute_scores()
    
    #! uncomment these to test it out
    #* First method of doing it  
    searchcommones = findmecommon(similarities)
    thebooks = recommendfinder(searchcommones)
    print(searchcommones)
    print(thebooks)
    
    #* Second method of doing it. if you wanted to get a huge list of everyones common reading types 
    #commons = sortme(similarities)
    #print(commons)
    pass

if __name__ == "__main__":
    main()

