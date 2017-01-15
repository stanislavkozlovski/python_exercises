#  https://www.hackerrank.com/challenges/greedy-florist
"""
The algorithm is the following:
Cycle the people and have them purchase the most expensive item each time
That way, the most expensive items get purchased with the lowest possible purchase counts
"""
flower_count, people = [int(p) for p in input().split()]
flower_prices = list(sorted([int(p) for p in input().split()]))

money_spent = 0
purchases_made = [1] * people  # hold the purchase count for each person
while flower_count > 0:
    # get the cheapest flower for each person
    for person in range(people):
        purchase_price = flower_prices.pop() * purchases_made[person]
        purchases_made[person] += 1
        money_spent += purchase_price
        flower_count -= 1
        if flower_count == 0:
            break

print(money_spent)