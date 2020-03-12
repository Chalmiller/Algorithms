def square_digits(num):
    new_string = ""
    for digit in str(num):
        new_string += str(int(digit)**2)
    return new_string

square_digits(9119)