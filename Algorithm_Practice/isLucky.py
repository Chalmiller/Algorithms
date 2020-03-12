def isLucky(n):
    num_list = [int(num) for num in str(n)]
    middle = len(num_list)//2
    if sum(num_list[:middle]) == sum(num_list[middle:]):
        return True
    else:
        return False

n = 1230
isLucky(n)