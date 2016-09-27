"""
The bike costs K dollars. At the start of every day I save up N dollars
and at the start of every 10 days I spend M dollars.
Output the days it'll take to save up for the bike.
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
# 100/100, tried with Decimal rather than float for more precision, but the results are the same.


def get_day(days_passed: int, savings: float, bike_price: float, daily_wage: float) -> int:
    """
    This function is called when we have enough money for a bike. Due to the nature of our program, most likely
    we will have a surplus of money and will need to calculate backwards to pinpoint the exact moment we saved up
    exactly enough for the bike. This function calculates backwards and outputs the specific day to the console.
    After which, closes the program because that is all that is required from this exam problem.
    """
    while savings - daily_wage >= bike_price:
        savings -= daily_wage
        days_passed -= 1

    print(days_passed)
    exit()


def main():
    try:
        bike_price = float(input())
        daily_saved = float(input())  # the dollars_saved we save up every day
        dollars_spent = float(input())  # the dollars_saved I spend every 10 days

        if bike_price < 0 or daily_saved < 0 or dollars_spent < 0:
            # the input is invalid
            raise Exception

        days_passed = 0
        savings = float(0)

        # 1. Have 9 days pass
        savings += daily_saved * 9
        days_passed += 9

        if savings >= bike_price:
            get_day(days_passed, savings, bike_price, daily_saved)

        # 2. Check if we aren't losing money each 10 days
        if (daily_saved * 10) - dollars_spent <= 0.0:
            print("NO BIKE FOR YOU")
            exit()

        # Now we know that we have a surplus of money and will eventually save up for the bike
        # 3. Have 10 days pass in a loop until we get at the desired amount
        while True:
            savings += (daily_saved * 10) - dollars_spent
            days_passed += 10

            if savings >= bike_price:
                get_day(days_passed, savings, bike_price, daily_saved)

    except Exception:
        print("INVALID INPUT")

if __name__ == '__main__':
    main()
