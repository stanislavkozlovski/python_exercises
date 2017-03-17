#  https://www.hackerrank.com/challenges/mark-and-toys

_, money = [int(p) for p in input().split()]
sorted_toys = sorted([int(p) for p in input().split()])
bought_toys = 0
for toy_price in sorted_toys:
    if toy_price > money:
        break
    money -= toy_price
    bought_toys += 1
print(bought_toys)