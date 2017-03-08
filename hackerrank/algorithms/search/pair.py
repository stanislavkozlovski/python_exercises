# https://www.hackerrank.com/challenges/pairs?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
from collections import Counter

_, k = [int(p) for p in input().split()]
numbers = [int(p) for p in input().split()]
occurences = Counter(numbers)

pair_count = 0
for num in numbers:
    pair_count += occurences.get(num+k, 0)
print(pair_count)