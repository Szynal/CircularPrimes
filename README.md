# CircularPrimes
 "Circular Prime" program in python


## Task assumptions

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.


> OBJECTIVES

 * There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. 
 * How many circular primes are there below one million?


##  Getting started

### 1. Find prime numbers (classic academic problem) 

  Sieve of Eratosthenes -> "In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit."

  https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


 Code in python
 
   ```python
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

 ```
 ### 2. Number variation without repetition (Wariacja bez powtórzeń [PL])
 
 itertools.combinations is what I need...
 
 https://www.kite.com/python/docs/itertools.combinations
 Return r length subsequences of elements from the input iterable.

 this solution caused all permutations and we just needed to rearrange the numbers..


   ```python
def get_iter_combinations( number ):
    str_nr = list(str(number))
    numbers = []
    for i in range(len(str_nr)):
        str_nr.append(str_nr.pop(str_nr.index(str_nr[0])))
        a = ''.join(str_nr)
        print(str_nr)
        numbers.append(a)
    print(numbers)

 ```
This solution ignores zeros and repetitions. For example: 111 or 700 -> 070, 007

### 2. Full Solution


   ```python
def sieve_of_eratosthenes( number ):
    counter = 0
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
            local_counter = 0
            p_combinations = get_iter_combinations(p)
            for n in p_combinations:
                re_roll_number = int(n)
                if prime[re_roll_number]:
                    local_counter = local_counter + 1
            if local_counter == len(p_combinations):
                counter = counter + 1
    return counter


def get_iter_combinations( number ):
    str_nr = list(str(number))
    numbers = []
    for i in range(len(str_nr)):
        str_nr.append(str_nr.pop(str_nr.index(str_nr[0])))
        a = ''.join(str_nr)
        while a[:1] == '0':
            a = a[1:]
        if a in numbers:
            continue
        numbers.append(a)
    return numbers

 ```
  
## 3.Complexity
### Time complexity	:
O((n * log * log(n))
### Memory complexity	:
O(n)
