def arrayChange(inputArray):
    if inputArray == sorted(inputArray):
        return 1
    else:
        for i in range(len(inputArray) - 1):
            if inputArray[i] >= inputArray[i+1]:
                inputArray[i+1] += 1
                return i + arrayChange(inputArray)

inputArray = [1, 1, 1]
arrayChange(inputArray)