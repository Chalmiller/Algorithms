def firstNotRepeatingCharacter(s):

    myList = list()
    for el in s:
        if s.index(el) == s.rindex(el):
            return el
    return '_'


s = "abacabad"
firstNotRepeatingCharacter(s)