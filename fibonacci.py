"""
Fibonacci numbers in Python
"""

def fibonacciNumbers(x):

    # Since we know the conditions require the list to begin with the values 0
    # and 1 we can safely assert this is the initial case
    fibonacciList = [0,1]

    for i in range(2, x+1):
        fibonacciList.append(fibonacciList[i-1]+fibonacciList[i-2])

    print(fibonacciList[x])


if __name__ == "__main__":
    fibonacciNumbers(24)
