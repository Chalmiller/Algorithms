def firstDuplicate(a):
    # generate a new empty set
    mySet = set()
    # iterate over the input list
    for el in a:
        # if the element exists within the set already, it will be the lowest indexed item within it.
        # We should therefore return it to the output.
        if el in mySet:
            return el
        # Add the element to the set if it is not already present.
        mySet.add(el)
    return -1

a = [2, 1, 3, 5, 3, 2]
firstDuplicate(a)