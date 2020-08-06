import itertools,random

def online_random_sample(it, k):
    sampling_results = list(itertools.islice(it,k))
    num_so_far = k
    for x in it:
        num_so_far += 1
        idx_to_replace = random.randrange(num_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x
    return sampling_results

print(online_random_sample([12,13,15,155,6,7,2,532,2],5))
