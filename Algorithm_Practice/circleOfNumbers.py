def circleOfNumbers(n, firstNumber):
    if n == 0:
        return 0
    else:
        halfway_point = n // 2
        radially_opposite = firstNumber + halfway_point if firstNumber < halfway_point else firstNumber - halfway_point
        return radially_opposite

n = 10
first = 2
circleOfNumbers(n, first)
