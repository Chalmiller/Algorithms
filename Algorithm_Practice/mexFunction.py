def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound

    return found

s = [2, 3, 6, 34, 56, 7]
upperBound = 1
mexFunction(s, upperBound)