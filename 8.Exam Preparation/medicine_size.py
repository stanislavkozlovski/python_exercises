import csv

INDEX_M_NAME = 0
INDEX_M_WIDTH = 1
INDEX_M_HEIGHT = 2
INDEX_M_DIAMETER = 3

"""
minimum dimension of A < minimum dimension of B &&
median dimension of A < median dimension of B  &&
maximum dimension of A < maximum dimension of B
 """
try:
    width = float(input())
    height = float(input())
    diameter = float(input())
    file_name = input()

    temp_box_list = [width, height, diameter]
    temp_box_list = sorted(temp_box_list)
    minimum_dimension_box = temp_box_list[0]
    median_dimension_box = temp_box_list[1]
    maximum_dimension_box = temp_box_list[2]

    with open(file_name, encoding='utf-8') as _:
        file_reader = csv.reader(_)

        for line in file_reader:
            if line:  # if it's not an empty line
                medicine_name = line[INDEX_M_NAME]
                medicine_width = float(line[INDEX_M_WIDTH])
                medicine_height = float(line[INDEX_M_HEIGHT])
                medicine_diameter = float(line[INDEX_M_DIAMETER])

                temp_medicine_list = [medicine_width, medicine_height, medicine_diameter]
                temp_medicine_list = sorted(temp_medicine_list)
                minimum_dimension_medicine = temp_medicine_list[0]
                median_dimension_medicine = temp_medicine_list[1]
                maximum_dimension_medicine = temp_medicine_list[2]

                if (minimum_dimension_medicine <= minimum_dimension_box
                    and median_dimension_medicine <= median_dimension_box
                    and maximum_dimension_medicine <= maximum_dimension_box):
                    print(medicine_name)


except Exception:
    print("INVALID INPUT")
