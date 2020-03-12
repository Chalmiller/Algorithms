def adjacentElementsProduct(inputArray):

    product = inputArray[0] * inputArray[1]
    for el in range(len(inputArray) - 1):
      temp = inputArray[el] * inputArray[el + 1]
      if temp > product:
          product = temp
      else:
          continue
    return product