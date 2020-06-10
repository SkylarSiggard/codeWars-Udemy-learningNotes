#my way of doing it even tho i should have used map() i figured out how to do it even tho  im not sure 

def duplicate_count(text):
    lettersUsed = []
    multipleLetters = []
    total = 0
    for i in text.lower():
        if i not in lettersUsed:
            lettersUsed.append(i)
        else:
            multipleLetters.append(i)
    for j in lettersUsed:
        if j in multipleLetters:
            total += 1
        else:
            pass
    return total

duplicate_count("indivisibilities")
duplicate_count("abcdea")
duplicate_count("abcde")

#! how people did it online! they are so good and clean
def duplicate_count2(s):
    return len([c for c in set(s.lower()) if s.lower().count(c)>1])

def duplicate_count3(text):
    seen = set()
    dupes = set()
    for char in text:
        char = char.lower()
        if char in seen:
            dupes.add(char)
        seen.add(char)
    return len(dupes)

#from collections import Counter

#def duplicate_count4(text):
    #return sum(1 for c, n in Counter(text.lower()).iteritems() if n > 1)

def duplicate_count5(text):
    count = 0
    for c in set(text.lower()):
        if text.lower().count(c) > 1:
            count += 1
    return count