def numberMinimization(n, d):
    smallest = 0
    current_permutation = []
    if n % d == 0:
        smallest = n % d
    # generate a list representation of the number n to create permutations
    string_list = str(n).split()
    for i in range(len(string_list)):
        m = string_list[i]

        remLst = string_list[:i] + string_list[i+1:]