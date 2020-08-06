'''
Given an array A of n elements and permutation P, apply P to A
'''

def permutate(A, P):
    for i in range(len(A)):
        next = i
        while P[next] >= 0:
            A[i], A[P[i]] =  A[P[i]], A[i]
            temp = P[next]
            P[next] -= len(P)
            next = temp
    P[:] = [a + len(P) for a in P ]
    print(A)
permutate(['a','b','c','d'],[2,0,1,3])