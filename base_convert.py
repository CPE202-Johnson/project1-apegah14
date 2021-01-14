def convert(num, b):
    if num // b == 0:
        converted_num = []
    else:
        remainder = num % b
        quotient = num // b
        converted_num = convert(quotient, b) + [remainder]
    return converted_num

if __name__ == "__main__":
    print(convert(13, 2))