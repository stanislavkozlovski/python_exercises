# https://www.hackerrank.com/challenges/bon-appetit
_, k = [int(part) for part in input().split()]

items = [int(part) for part in input().split()]
anna_bill = (sum(items) // 2) - (items[k] // 2)  # the amout anna should pay

charged_money = int(input())

if charged_money == anna_bill:
    print('Bon Appetit')
else:
    print(charged_money - anna_bill)