'''
WAP that takes array A of n numbers and rearragnes A's elements to get a new array B having the property that
B[0] <= B[1] >= B[2] <= B[3}] ....
'''

def my_method_alter(A):
    sortedA = sorted(A)
    B = [0] * len(A)
    cnt = 0
    for i in range(0,len(A),2):
        B[i] = sortedA[cnt]
        cnt += 1
    for i in range(1, len(A),2):
        B[i] = sortedA[cnt]
        cnt += 1
    return B

# BOOK METHOD
def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)
        print(A)


print(my_method_alter([5,4,3,2,1]))
print(rearrange([5,4,3,2,1]))