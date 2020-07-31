# CHECK IF DECIMAL INTEGER IS PALINDROME OR NOT
# RETURN TRUE OR FALSE ie. for 123 return false and 111 return true
def palidrome_check(x):
    num = 0
    ox = abs(x)
    while ox:
        num = num * 10 + (ox % 10)
        ox //= 10
    rev_num = num if x >= 0 else -num
    return rev_num == x


print(palidrome_check(111))
