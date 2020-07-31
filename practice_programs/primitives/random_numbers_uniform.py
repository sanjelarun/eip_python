import random


def uniform_random_generator(lower, upper):
    no_of_outcomes = upper - lower + 1
    while True:
        result, i = 0, 0
        while (1 << i) < no_of_outcomes:
            result = (result << 1) | random.randrange(0,2)
            i += 1
        if result < no_of_outcomes:
            break
    return result + lower

print(uniform_random_generator(1,6))