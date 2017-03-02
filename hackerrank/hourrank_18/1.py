"""
5 3
2 5
7 10
2 9
"""
m, n = [int(p) for p in input().split()]
marbles = [False for _ in range(11)]
marbles[m] = True
for _ in range(n):
    a, b = [int(p) for p in input().split()]
    marbles[a], marbles[b] = marbles[b], marbles[a]
print(marbles.index(True))