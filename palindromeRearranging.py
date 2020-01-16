def palindromeRearranging(inputString):

    def permutation(lst):
        if len(lst) == 0:
            return []
        if len(lst) == 1:
            return [lst]
        end_list = []
        for j in range(len(lst)):
            m = lst[j]
            rem_lst = lst[:j] + lst[j+1:]
            for p in permutation(rem_lst):
                end_list.append([m] + p)
        return end_list

    my_list = permutation(list(inputString))
    is_permutation = False
    for i in my_list:
        if i == i[::-1]:
            is_permutation = True
            print(True)
            break
    print(is_permutation)
    return is_permutation

inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"
palindromeRearranging(inputString)
