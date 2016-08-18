"""
За колко време ще пристигне автомобил от град А до град Б, ако спазва стриктно всички ограничения на скоростта, и се абстрахираме от други фактори?

Като входни данни се подава име на файл, в който на всеки ред се съдържат 3 полета:

километър от - включително - int
километър до - включително - int
ограничение на скоростта в този участък, в километри в час (км/ч)
Резултатът трябва да бъде в десетични часове, т.е. 2.5 (което означава 2 часа 30 минути) , или 2.25 (което означава 2 часа и 15 минути) и т.н. Изведете резултата с точност до 2 знака след десетичния знак.

Ако подадените данни са невалидни, трябва да изведете INVALID INPUT
"""

import csv

INDEX_FILE_KM_FROM = 0
INDEX_FILE_KM_TO = 1
INDEX_FILE_KMPH = 2

try:
    file_name = input()
    result = 0

    with open(file_name, encoding='utf-8') as _:
        f_reader = csv.reader(_)
        """
        read each line, calculate the time it would take from km a to km b
        (
        by finding the km needed to be traveled (b - a +1) ex: (40-39 + 1).
        From 39-40 there are 2 kilometers because we're counting as if we've passed the 40th
        too. Then, dividing that by the speed limit to see how much time it takes.
        ex: 2 divided by a speed limit of 2 is 1
        Which, coincidentally, is 1 hour according to the expected output. 2 divided by a speed limit of 4 is 0.5, which
        is half an hour according to the expected output.
        )
        then, add it to the overall time it would take to cross from the first point in the file to the last one
        Finally, print the overall time
        """
        for line in f_reader:
            km_from = float(line[INDEX_FILE_KM_FROM])
            km_to = float(line[INDEX_FILE_KM_TO])
            kmph = float(line[INDEX_FILE_KMPH])

            result += (km_to - km_from + 1) / kmph

    print("{:.2f}".format(result))
except Exception:
    print("INVALID INPUT")