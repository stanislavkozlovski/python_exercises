"""
Given a .csv file that holds information on temperature measurements of cities, print out the dates
that are missing for a certain city.
"""
import csv


INDEX_DATE = 0
INDEX_CITY = 1
INDEX_TEMPERATURE = 2


def main():
    """

    """
    try:
        file_path = input()

        # load a dict key: date value: city, a sorted list of dates type: list and the cities type: set
        whole_file_dict, list_of_dates, list_of_cities = load_from_file(file_path)
        # missing_dates will hold key: Date(str) that's missing, Value: a list of the cities which are missing said date
        missing_dates = {}  # type: dict

        for date in list_of_dates:
            # iterate through all the dates

            for city in list_of_cities:
                # iterate through all the cities, effectively every date/city combination

                if city not in whole_file_dict[date]:  # if the city does not have records for said date
                    # add the date and city to the missing dates
                    if date not in missing_dates.keys():
                        missing_dates[date] = []
                    missing_dates[date].append(city)

        # at the end, print the missing dates
        print_missing_dates(missing_dates)
    except Exception as e:
        print("INVALID INPUT")


def load_from_file(file_path: str) -> tuple:
    """
    Here we read from the csv files, fill and return three collections
    1 - whole_file_dictionary: A dictionary Key: the date of the temperature measurement as a string,
                                            Value: The city as a string
    2 - at the start a SET of all the dates, which we later convert to a list and sort the dates in ascending order
    3 - a set of all the cities
    :param file_path: the path to the .csv file we'll be reading from
    :return: Tuple(1,2,3)
    """
    is_empty = True
    whole_file_dictionary = {}
    cities, dates = set(), set()

    with open(file_path, encoding='utf-8') as _:
        data_reader = csv.reader(_)
        for line in data_reader:
            if line:  # if it's not an empty line
                is_empty = False
                date = line[INDEX_DATE]
                city = line[INDEX_CITY]

                if date not in whole_file_dictionary.keys():
                    whole_file_dictionary[date] = []

                whole_file_dictionary[date].append(city)
                cities.add(city)
                dates.add(date)

    if is_empty:
        raise Exception("The .csv file cannot be empty!")
    ordered_dates = list(dates)
    ordered_dates.sort()

    return whole_file_dictionary, ordered_dates, cities


def print_missing_dates(missing_dates: dict):
    printed_anything = False
    ordered_dates = list(missing_dates.keys())
    ordered_dates = sorted(ordered_dates)

    for date in ordered_dates:
        # if we have such a missing date and it's list is not empty
        if date in missing_dates.keys() and missing_dates[date]:
            print("{date},{cities}".format(date=date, cities=','.join(sorted(missing_dates[date]))))
            printed_anything = True
    if not printed_anything:
        print("ALL DATA AVAILABLE")

if __name__ == "__main__":
    main()