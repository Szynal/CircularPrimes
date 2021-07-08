# This is a sample Python script.

def sieve_of_eratosthenes( number ):
    prime = [True for i in range(number + 1)]
    p = 2
    while p * p <= number:
        if prime[p]:
            for i in range(p * 2, number + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(number + 1):
        if prime[p]:
            print(p)


if __name__ == '__main__':
    n = 30
    sieve_of_eratosthenes(n)
