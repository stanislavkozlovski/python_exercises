"""
Given a product's ID and a sales text document. Find the city from which the item has been sold for the lowest price.

Sample input:
G17628
1-sales.txt
"""
import csv

INDEX_SALES_PRODUCT_ID = 0
INDEX_SALES_CITY = 2
INDEX_SALES_PRICE = 4

target_product_id = input()
sales_file_name = input()


with open(sales_file_name, encoding='utf-8') as _:
    sf_reader = csv.reader(_)
    # get a list of tuples with sales only for the product we're searching for
    sales_filtered = filter(lambda sale: sale[INDEX_SALES_PRODUCT_ID] == target_product_id, sf_reader)
    # get the sale with the minimum price and print the city from it
    print(min(sales_filtered, key=lambda x: x[INDEX_SALES_PRICE])[INDEX_SALES_CITY])