"""
The bike costs K dollars. At the start of every day I save up N dollars
and at the start of every 10 days I spend M dollars.
Output the day it'll take to save up for the bike.
If I cannot buy the bike (I spend more than I earn, output "NO BIKE FOR YOU"

ex input:
100
3.50
8
ex output:
36

ex input 2:
100
3
35
ex output 2:
NO BIKE FOR YOU
"""

try:
    bike_price = int(input())
    dollars_saved = float(input())  # the dollars we save up every day
    dollars_spent = int(input())  # the dollars I spend every 10 days

    days_passed = 0
    dollars = 0
    while True:
        dollars += dollars_saved
        days_passed += 1

        if days_passed % 10 == 0:
            dollars -= dollars_spent

        if dollars >= bike_price:
            print(days_passed)
            break

        if dollars <= 0:
            print("NO BIKE FOR YOU")

except Exception:
    print("INVALID INPUT")