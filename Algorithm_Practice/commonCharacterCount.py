def commonCharacterCount(s1, s2):
    sum_of_characters = 0
    character_set = {char for char in s1}

    for char in character_set:
        if char in s2:
            sum_of_characters += s1.count(char) if s1.count(char) < s2.count(char) else s2.count(char)

    return sum_of_characters

s1 = "aabcc"
s2 = "adcaa"
commonCharacterCount(s1,s2)