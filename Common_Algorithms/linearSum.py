def linearSum(S, n):
    if n == 0:
        return 0
    else:
        return linearSum(S, n - 1) + S[n - 1]