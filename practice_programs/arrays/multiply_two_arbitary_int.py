'''
WAP that takes two arrays representing integers, and returns an integer representing their product
Example <1,2> and <2> returns <2,4>
'''
import time


# MY METHOD : Convert into single int and do multiplication
def multiply_two_list(A, B):
    sign = -1 if A[0] < 0 or B[0] < 0 else 1
    A[0], B[0] = abs(A[0]), abs(B[0])
    num1 = 0
    prod = 1
    for i in reversed(A):
        num1 += (i * prod)
        prod *= 10
    product = 1
    result = 0
    for i in reversed(B):
        result += (i * num1 * product)
        product *= 10
    conver_list = [int(i) for i in str(result)]
    return [conver_list[0] * sign] + conver_list[1:]


# BOOK METHOD
def multiply(A, B):
    sign = -1 if A[0] < 0 or B[0] < 0 else 1
    A[0], B[0] = abs(A[0]), abs(B[0])
    result = [0] * (len(A) + len(B))
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            result[i + j + 1] += A[i] * B[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]


start_time = time.time()
print(multiply_two_list([1, 9, 3, 7, 0, 7, 7, 2, 1,2,2,2,2,2,2], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]))
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
print(multiply([1, 9, 3, 7, 0, 7, 7, 2, 1,2,2,2,2,2,2], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]))
print("--- %s seconds ---" % (time.time() - start_time))
