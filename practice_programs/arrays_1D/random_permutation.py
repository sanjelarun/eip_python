import random
def random_perm(n):
    perm = [0] * n
    swap_index = n-1
    random_list  = list(range(n))
    index = n
    for i in range(n):
        random_int = random.randrange(index)
        perm[i] = random_list[random_int]
        random_list[random_int], random_list[swap_index] = random_list[swap_index], random_list[random_int]
        index -= 1
        swap_index -= 1
    return perm

print(random_perm(5))
