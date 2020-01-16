def matrixElementsSum(matrix):
    zipped_matrix = list(zip(*matrix))

    sum = 0
    for lists in zipped_matrix:
        for num in lists:
            if num == 0:
                break
            else:
                sum += num
    return sum

matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]
matrixElementsSum(matrix)
