import random
def random_sample(k,A):
    for i in range(k):
        r =random.randint(i, len(A) - 1)
        A[i], A[r] =A[r], A[i]


A = [2,5,6,12,59,31,21,32,62,12]
random_sample(4,A)
print(A)