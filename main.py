counter = 0


def sieve_of_eratosthenes(number):
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
            if (local_counter == len(p_combinations)):
                counter = counter + 1
    return counter


def get_iter_combinations(number):
    str_nr = list(str(number))
    numbers = []
    for i in range(len(str_nr)):
        str_nr.append(str_nr.pop(str_nr.index(str_nr[0])))
        a = ''.join(str_nr)
        while a[:1] == '0':  # Wywalanie  zer  ['1', '10', '100', '1000', '10000', '100000', '1000000'] dla np miliona
            a = a[1:]
        if a in numbers:  # dla  np 111
            continue
        numbers.append(a)
    return numbers


if __name__ == '__main__':
    n = 100
    print(sieve_of_eratosthenes(n))
