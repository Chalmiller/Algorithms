def sortByHeight(a):
    newList = []
    pos_nums = sorted(list(filter(lambda  x: x >= 0, a)))

    for i in range(len(a)):
        if a[i] == -1:
            newList.append(a[i])
        else:
            newList.append(pos_nums.pop(0))

    return newList

a = [-1, 150, 190, 170, -1, -1, 160, 180]
sortByHeight(a)