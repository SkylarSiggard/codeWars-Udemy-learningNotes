def solution(s):
    if len(s) == 0:
        return []
    else:
        takeTwo = [s[i:i + 2] for i in range(0, len(s), 2)]
    if len(takeTwo[-1]) == 1:
        takeTwo[-1] = takeTwo[-1] + '_'
        return takeTwo
    else:
        return takeTwo
solution('alkjflkdsaj')
solution('adfsda')

#! how others did it:
def solution2(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
    return result


def solution3(s):
    return [s[x:x+2] if x < len(s) - 1 else s[-1] + "_" for x in range(0, len(s), 2)]

