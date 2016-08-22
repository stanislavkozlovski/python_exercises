"""
You have a smart refridgerator, from which you can access it's temperature inside.
Write a program, which shows when the fridge has been opened.
When the fridge is opened, the temperature inside increases by at least 4 degrees
Input is the path to the .csv file, which contains the information
"""
from csv import reader

INDEX_TIME = 0
INDEX_TEMP = 1

file_path = input()

with open(file_path, encoding='utf-8') as _:
    fridge_log = list(reader(_))

    temperatures = [float(l[INDEX_TEMP]) for l in fridge_log]
    #  get the differences between the temperatures and store the indexes where the difference was >= 4 (fridge opened)
    opened_indexes = [idx for idx, num in enumerate( [j - i for i, j in zip(temperatures[:-1], temperatures[1:])] )
                      if num >= 4]

    """
    cleaner solution using numpy
    opened_indexes = [idx for idx, num in enumerate(numpy.diff( [float(l[INDEX_TEMP]) for l in fridge_log] ))
                      if num >= 4]
    """

    for idx in opened_indexes:
        print(fridge_log[idx+1][INDEX_TIME])

# 100/100