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
import datetime
import re

DATE_PATTERN = r'(\d{4})-(\d{1,2})-(\d{1,2})'  # regex pattern for a valid date
INDEX_DATE = 0
INDEX_PRICE = 1

def parse_date(date_str: str) -> datetime.date:
    """
    This function tries to parse a presumably ISO-8601 formatted string to a datetime.date object
    Here, we also test to see if the date itself is valid, meaning if any number is negative or an invalid day/month
    :return: The string converted to a datetime.date object OR raise an exception
    """
    match = re.match(DATE_PATTERN, date_str)

    if match:
        date_year = int(match.group(1))
        date_month = int(match.group(2))
        date_day = int(match.group(3))

        # parsing to the date will throw an error itself if the year/month/day is invalid
        return datetime.datetime(date_year, date_month, date_day)
    else:
        # invalid date -> invalid input error
        raise Exception


try:
    records = 0
    is_drastic_change = False
    file_name = input()
    drastic_percent = float(input())
    output = []  # store the output and print it all out in the end.

    if drastic_percent <= 0:
        # INVALID INPUT
        raise Exception

    with open(file_name, encoding='utf-8') as _:
        file_reader = csv.reader(_)

        last_price = 0
        last_date = None

        for line in file_reader:
            date_str = line[INDEX_DATE]
            date = parse_date(date_str)
            price = float(line[INDEX_PRICE])

            if price < 0:
                # INVALID INPUT
                raise Exception
            if last_date:  # check if last date is assigned
                if (date-last_date).days < 0:  # check if the dates are not backwards
                    raise Exception

            if last_price and last_price <= price:  # check if last_price is assigned and if the new price is bigger
                difference = price-last_price
                percentage = round((difference / last_price) * 100, 2)
                if percentage >= drastic_percent:
                    output.append("{date} {percentage}".format(date=date_str, percentage=percentage))
                    is_drastic_change = True

            last_date = date
            last_price = price
            records += 1

    if is_drastic_change:
        print('\n'.join(output))
    else:
        print("NO DRASTIC CHANGES; RECORDS COUNT: {}".format(records))

except Exception as e:
    print("INVALID INPUT")