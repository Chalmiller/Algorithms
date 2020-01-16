def bitwise_operations(n, k):
    revised_bit = ""
    bit_integer = format(n, 'b')
    for digit in range(len(format(n, 'b'))):
        if digit == len(format(n, 'b')) - 3:
            revised_bit += str(0)
        else:
            revised_bit += bit_integer[digit]
    return int(revised_bit, 2)


n = 37
k = 3
bitwise_operations(n, k)