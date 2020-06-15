# to turn a word into a hash tag. 
def generate_hashtag(s):
    if len(s) == 0 or s == '#':
        return False
    else:
        caps = []
        x = s.split()
        for i in x:
            caps.append(i.capitalize())
        t = ''.join(caps)
        if len(t) + 1 < 140:
            return '#' + t
        else:
            return False



#! how others did it with cleaner code. Wanna get to that point. 
def generate_hashtag2(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False

def generate_hashtag3(s):
    ans = '#'+ str(s.title().replace(' ',''))
    return s and not len(ans)>140 and ans or False
