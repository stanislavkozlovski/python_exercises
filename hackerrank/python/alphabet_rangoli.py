# https://www.hackerrank.com/challenges/alphabet-rangoli


def build_middle_part(last_letter: str, n: int, overall_length: int):
    middle_part = []

    for i in range(1, n-1):
        # the middle part which goes on the left and right of the middle letter
        mid_letter = chr(ord(last_letter) - i)
        mid_part = '-'.join([chr(ord(mid_letter) + (part + 1)) for part in range(0, i)])

        mid = (''.join(reversed(mid_part)) + '-{}-'.format(mid_letter) + mid_part)

        # create the '-' that stay at both ends
        fill_len = (overall_length-len(mid)) // 2
        fill_annexation = '-' * fill_len

        middle_part.append(fill_annexation + mid + fill_annexation)

    return middle_part


def print_result(start_end, middle_part, center):
    print(start_end)
    if middle_part:
        print('\n'.join(middle_part))
    print(center)
    if middle_part:
        print('\n'.join(reversed(middle_part)))
    print(start_end)


def main():
    n = int(input())

    if n == 1:
        print('a')
        exit()

    last_letter = chr(96 + n)

    center_part = '-'.join([chr(96 + part) for part in reversed(range(2, n+1))])
    center = center_part + '-a-' + ''.join(reversed(center_part))
    overall_length = len(center)

    fill_annexation = '-' * ((overall_length - 3)//2)
    start_end = fill_annexation + '-{}-'.format(last_letter) + fill_annexation

    middle_part = build_middle_part(last_letter, n, overall_length)

    print_result(start_end, middle_part, center)


if __name__ == '__main__':
    main()
