"""
Given a .csv file holding information about sales, find the sales that are unique (that have been sold in one city only)
"""
import csv


def main():
    try:
        file_path = input()
        city_sales = {}  # type: dict
        id_sales = {}  # type: dict
        id_sales_keys = []  # this will hold the sale_id in the order they were given
        with open(file_path, encoding='utf-8') as _:
            sales_reader = csv.reader(_)
            file_is_empty = True
            for line in sales_reader:
                if line:
                    file_is_empty = False
                    sale_id = line[0]
                    sale_city = line[2]

                    if sale_city not in city_sales.keys():
                        # initiate a list if one hasn't been initiated
                        city_sales[sale_city] = set()

                    city_sales[sale_city].add(sale_id)

                    if sale_id not in id_sales.keys():
                        # initiate a list if one hasn't been initiated
                        id_sales_keys.append(sale_id)
                        id_sales[sale_id] = set()


                    id_sales[sale_id].add(sale_city)

        if file_is_empty:
            raise Exception("The .csv file should not be empty!")

        unique_sales = filter_unique_sales(id_sales, id_sales_keys)

        # sort the cities alphabetically and then proceed to print
        unique_sales_ordered_cities = sorted(list(unique_sales.keys()))
        are_unique_sales = False
        for city in unique_sales_ordered_cities:
            print("{},{}".format(city, ','.join(sorted(unique_sales[city]))))
            are_unique_sales = True

        if not are_unique_sales:
            print("NO UNIQUE SALES")
    except Exception as e:
        print("INVALID INPUT")


def filter_unique_sales(id_sales: dict, id_sales_keys: list) -> dict:
    unique_sales = {}  # key: city, value: list of numbers

    for sale_id in id_sales_keys:
        sale_cities = id_sales[sale_id]
        if len(sale_cities) == 1:
            city = sale_cities.pop()
            if city not in unique_sales.keys():
                unique_sales[city] = []

            unique_sales[city].append(sale_id)

    return unique_sales

if __name__ == "__main__":
    main()

#   100/100