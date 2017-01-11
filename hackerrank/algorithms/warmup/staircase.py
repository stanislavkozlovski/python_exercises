#  https://www.hackerrank.com/challenges/staircase
print('\n'.join((' '*(n-i) + '#'*i) for i in range(1, int(input()) + 1)))
n = int(input())

for i in range(1, n+1):
    spaces = ' ' * (n - i)
    hashtags = '#' * i
    print(spaces + hashtags)