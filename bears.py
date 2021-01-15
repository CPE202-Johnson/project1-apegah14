# int -> boolean
# determine whether or not the game can be won with a specified number of bears
def bears(n):
    if n == 42:
        return True
    elif n == 0:
        return False
    else:
        nums = [0, 0, 0]
        if n % 2 == 0:  # n is even
            nums[0] = n // 2
        if n % 3 == 0 or n % 4 == 0:  # n is divisible by 3 or 4
            last_two = n % 100  # get last 2 digits of n
            ones = last_two % 10
            tens = last_two // 10
            nums[1] = n - (ones * tens)
        if n % 5 == 0:  # n is divisible by 5
            nums[2] = n - 42
        for num in nums:
            if bears(num) is True:
                return bears(num)