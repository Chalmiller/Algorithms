def makeArrayConsecutive2(statues):
    extra_statues = 0
    sorted_statues = sorted(statues)
    print(sorted_statues)
    for el in range(len(statues) - 1):
        if (sorted_statues[el + 1] - sorted_statues[el]) > 1:
            extra_statues += (sorted_statues[el + 1] - sorted_statues[el] - 1)
    return extra_statues


statues = [6, 2, 3, 8]
makeArrayConsecutive2(statues)