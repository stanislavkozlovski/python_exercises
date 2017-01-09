#  https://www.hackerrank.com/challenges/acm-icpc-team


def get_equal_count(bin_a, bin_b):
    """
    Having two binary numbers - 0010 and 0101 - return the sum of 1s as if we've used a logical OR on them
    """
    return len([a for a in str(bin((int(bin_a, 2) | int(bin_b, 2))))[2:] if a == '1'])

n, m = [int(part) for part in input().split()]
people = []
for _ in range(n):
    person = input()
    people.append(person)
    # 10101 11010

max_score = 0
max_teams = 0
for idx, person in enumerate(people):
    for idx_2 in range(idx+1, len(people)):
        score = get_equal_count(person, people[idx_2])
        if score > max_score:
            max_score = score
            max_teams = 0
        if score == max_score:
            max_teams += 1


print(max_score)
print(max_teams)
