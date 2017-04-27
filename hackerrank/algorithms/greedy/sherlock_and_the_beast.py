n = int(input())

for i in range(n):
    digit_len = int(input())
    starting_num = '5' * digit_len
    digits = {
        '5': digit_len,
        '3': 0
    }

    while digits['5'] % 3 != 0 or digits['3'] % 5 != 0:
        if digits['5'] == 0:
            break
        digits['3'] += 1
        digits['5'] -= 1

    if digits['5'] % 3 != 0 or digits['3'] % 5 != 0:
        print(-1)
    else:
        print('5' * digits['5'] + '3' * digits['3'])