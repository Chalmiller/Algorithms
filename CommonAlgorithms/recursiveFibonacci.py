def recursiveFibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a,b) = recursiveFibonacci(n-1)
        return (a+1, a)