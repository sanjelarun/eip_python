# REVERSE DIGIT
# Takes integer as input and reverse the integer i.e 42 into 24

def reverse_int(x):
    num = 0
    ox = abs(x)
    while ox:
        num = num * 10 + (ox % 10)
        ox //= 10
    return num if x >= 0 else -num
print(reverse_int(12390))
