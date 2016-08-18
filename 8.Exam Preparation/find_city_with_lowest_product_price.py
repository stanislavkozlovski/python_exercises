import csv
from sys import float_info

INDEX_SALES_PRODUCT_ID = 0
INDEX_SALES_CITY = 2
INDEX_SALES_PRICE = 4

placeholder = (float_info.max, 0)   # type: tuple for easy indexing
target_product_id = input()
sales_file_name = input()

lowest_price_dict = {}  # key: product_id, value: tuple (lowest_price: float, city_name: str)

with open(sales_file_name, encoding='utf-8') as _:
    sf_reader = csv.reader(_)

    for line in sf_reader:
        if line:
            product_id = line[INDEX_SALES_PRODUCT_ID]
            city_name = line[INDEX_SALES_CITY]
            price = float(line[INDEX_SALES_PRICE])

            # TODO: check <=
            if price < lowest_price_dict.get(product_id, placeholder)[0]:
                lowest_price_dict[product_id] = (price, city_name)
print(lowest_price_dict[target_product_id][1])