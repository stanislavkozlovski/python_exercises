def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i*i <= num:
        if num % i == 0 or num % (i+2) == 0:
            return False
        i += 6

    return True


def main():
    game_count = int(input())
    PRIMES = {
        1: []
        # key: end of list
        # value: list of primes
    }
    for _ in range(game_count):
        primes = []
        n = int(input())
        max_n = max([key for key in PRIMES.keys() if key <= n])
        if max_n == n:
            primes = PRIMES[n]
        else:
            primes.extend(PRIMES[max_n])
            start = max_n
            set_ = list(range(start+1,n+1))
            for num in set_:
                if is_prime(num):
                    primes.append(num)
            PRIMES[n] = primes
        if len(primes) == 0:
            print('Bob')
        elif len(primes) % 2 == 0:
            print('Bob')
        else:
            print('Alice')


if __name__ == '__main__':
    main()