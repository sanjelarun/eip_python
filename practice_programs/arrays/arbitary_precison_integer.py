# WAP which takes an input as array of digits encoding a non negative decimal integer D
# and updates the array to represt the integer D + 1 i.e <1,2,9>  -> <1,3,0>


def increase_digits(A):
    carry = 0
    i = len(A) - 1
    while i >= 0:
        if A[i] == 9:
            A[i] = 0
            i -= 1
            carry = 1
        else:
            A[i] += 1
            carry = 0
            break
    if carry == 1:
        A.insert(0, 1)


A = [1, 9, 9]
increase_digits(A)
print(A)
