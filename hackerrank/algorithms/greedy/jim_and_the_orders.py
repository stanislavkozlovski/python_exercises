#  https://www.hackerrank.com/challenges/jim-and-the-orders
print(*([str(x[0]) for x in sorted([(i, sum(int(p) for p in input().split())) for i in range(1, int(input()) + 1)], key=lambda x:x[1])]))