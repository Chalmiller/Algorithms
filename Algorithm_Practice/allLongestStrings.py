def allLongestStrings(inputArray):
    length_array = []
    for el in inputArray:
        length_array.append(len(el))

    long_string = max(length_array)
    for i in range(len(length_array)):
        if long_string == length_array[i]:
            yield inputArray[i]
        else:
            continue


inputArray = ["aba", "aa", "ad", "vcd", "aba"]
allLongestStrings(inputArray)