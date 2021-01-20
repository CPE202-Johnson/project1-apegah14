# int -> boolean
# determine whether or not the game can be won with a specified number of bears
def bears(n):
    if n == 42:     # success case
        return True
    elif n < 42:    # failure case
        return False
    else:
        nums = [0, 0, 0]
        if n % 2 == 0:  # n is even
            nums[0] = n // 2
        if n % 3 == 0 or n % 4 == 0:    # n is divisible by 3 or 4
            last_two = n % 100          # get last 2 digits of n
            ones = last_two % 10        # separate ones place
            tens = last_two // 10       # separate tens place
            if ones == 0 or tens == 0:
                nums[1] = 0
            else:
                nums[1] = n - (ones * tens)
        if n % 5 == 0:  # n is divisible by 5
            nums[2] = n - 42
        for num in nums:    # iterate through all rules
            if bears(num) is True:
                return True