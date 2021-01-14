# int int -> int
# converts a base 10 number into a base b number
def convert(num, b):
    if num // b == 0:   # base case
        if num > 9:     # convert to A-F in cases of values greater than 9
            num = chr(num + 55)
        converted_num = str(num)
    else:
        remainder = num % b     # int value for remainder
        if remainder > 9:       # convert to A-F in cases of values greater than 9
            remainder = chr(remainder + 55)
        quotient = num // b     # int for quotient value
        converted_num = str(convert(quotient, b)) + str(remainder)      # construct the converted value as a string
    return converted_num