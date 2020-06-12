#Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed 
#(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
#
#Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
#spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"


#! my way isnt the shortest but it works. I could have made it cleaner. 
def spin_words(sentence):
    breakup = list(sentence.split())
    result = []
    for i in breakup:
        if len(i) >= 5:
            result.append(i[::-1])
        else: 
            result.append(i)
    return ' '.join(result)
spin_words("Welcome hello world cant")

#* how others were able to do it 
def spin_words1(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)

#*  shortest one i saw. will be a good example to shorten up my code. 
def spin_words2(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


