def maxMultiple(divisor, bound):
    biggest = 0
    for number in range(bound + 1):
        if (number % divisor == 0) and number > biggest:
            biggest = number
    return biggest

divisor = 3
bound = 10
maxMultiple(divisor, bound)

