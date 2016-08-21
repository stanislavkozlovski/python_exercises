"""
Given a .csv file with the ordered dates of sale and the price of the stock, print the ones that have jumped
more than X percent since the following day
Input is, on different lines, the path to the file and the percentage we count as drastic

sample input:
test-data-1.csv
10.02

sample output:
2016-07-19 10.46
2016-07-21 14.29

sample input 2:
test-data-2.csv
21

sample output 2:
NO DRASTIC CHANGES; RECORDS COUNT: 3
"""
import csv
import iso8601

INDEX_DATE = 0
INDEX_PRICE = 1
# TODO: save output in a string and print it at the end, in case the dates have different days, we need to print invalid input and probably not have anything else be printed out before hand
try:
    records = 0
    is_drastic = False
    file_name = input()
    drastic_percent = float(input())

    with open(file_name, encoding='utf-8') as _:
        file_reader = csv.reader(_)

        last_price = 0
        last_date = None

        for line in file_reader:
            date_str = line[INDEX_DATE]
            date = iso8601.parse_date(date_str)
            price = float(line[INDEX_PRICE])

            if last_price and last_price <= price:  # check if last_price is assigned and if the new price is bigger
                difference = price-last_price
                percentage = round((difference / last_price) * 100, 2)
                if percentage >= drastic_percent:
                    print("{date} {percentage}".format(date=date_str, percentage=percentage))
                    is_drastic = True

            if last_date:  # check if last date is assigned
                if (date-last_date).days is not 1:  # check if the dates are not one day apart
                    print("INVALID INPUT")
                    break

            last_date = date
            last_price = price
            records += 1

    if not is_drastic:
        print("NO DRASTIC CHANGES; RECORDS COUNT: {}".format(records))
except Exception:
    print("INVALID INPUT")