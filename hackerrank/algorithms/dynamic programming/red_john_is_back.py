def sieve(n):
    """ Return the amount of primes up until (and including) N"""
    count = 0
    not_prime = set()
    for i in range(2, n+1):
        if i not in not_prime:
            count += 1
            for j in range(i*i, n+1, i):
                not_prime.add(j)

    return count


def calculate_arrange_count(width):
    """
    There are two ways to arrange a wall of 4x4 with 1x4 and 4x1 blocks,
              one way for a wall of 4x(1-4)

    Further, the ways to arrange a wall of 4x15 is the sum of ways to arrange
        a 4x11 wall, where we've filled a 4x4 wall with 1x4's
        and
        a 4x14 wall, where we've filled a 4x1 wall with 4x1
    """
    if width < 0:
        return 0
    elif width < 4:
        return 1
    elif width == 4:
        return 2

    return calculate_arrange_count(width-1) + calculate_arrange_count(width-4)

test_count = int(input())
for _ in range(test_count):
    n = int(input())
    print(sieve(calculate_arrange_count(n)))
