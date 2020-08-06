'''
Enumerate all primes between 1 and N where N is provide by user
'''

def enumerate_primes(N):
    primes = []
    ch_primes = [True] * (N+1)
    for p in range(2, N+1):
        if ch_primes[p]:
            primes.append(p)
            for i in range(p,N+1,p):
                ch_primes[i] = False
    return primes

print(enumerate_primes(101))

