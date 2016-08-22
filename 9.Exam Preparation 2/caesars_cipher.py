"""
Given a key K, cipher a message's each LATIN UPPER-CASE LETTER K steps to the left.
 If it goes over the alphabet (31) just start from 1.

sample:
Нормална азбука:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ключ: 13
Шифрираща азбука: N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
"""


def exceed(position: int, min_pos, max_pos):
    """
    Recursive function to start over when the position + key exceeds the alphabet.
    :param position: the position we are at
    :param min_pos: the start position of the alphabet
    :param max_pos: the end position of the alphabet
    :return: the position we've ended up at as a result of all the starting over
    """
    if position > max_pos:
        exceeded = position - max_pos  # get the difference
        position = (min_pos-1) + exceeded  # start at the stand and add the difference
        position = exceed(position, min_pos, max_pos)  # check if we'

    return position

try:
    min_threshold, max_threshold = 65, 90
    key = int(input())
    message = input()

    for char in message:
        char_pos = ord(char)
        if min_threshold <= char_pos <= max_threshold:
            char_pos += key

            if char_pos > max_threshold:  # if we've exceeded the alphabet, start over
                char_pos = exceed(char_pos, min_threshold, max_threshold)

        print(chr(char_pos), end='')

except Exception:
    print("INVALID INPUT")

# 100/100 score


