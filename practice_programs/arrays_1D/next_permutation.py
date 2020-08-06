def next_permutation(P):
    swap_index = len(P) - 2
    while swap_index >= 0 and P[swap_index] >= P[swap_index + 1]:
        swap_index -= 1
    if swap_index == -1: return []
    for i in reversed(range(swap_index + 1, len(P))):
        if P[i] > P[swap_index]:
            P[i], P[swap_index] = P[swap_index], P[i]
            break
    P[swap_index+1:] = reversed(P[swap_index+1:])
    return P

print(next_permutation([1,2,3,0]))