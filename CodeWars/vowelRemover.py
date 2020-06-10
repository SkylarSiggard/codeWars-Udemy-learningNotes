def disemvowel(string):
    noTroll = ''
    vowels = ['a','e','i','o','u','y','A','E','I','O','U','Y']
    for i in string:
        if i not in vowels:
            noTroll += i
    return noTroll

disemvowel("This website is for losers LOL!")