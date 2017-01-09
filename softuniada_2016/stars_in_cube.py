def test_in_middle(matrix, row_idx, col_idx, symbol):
    top, left, right, bot, center = [False, False, False, False, False]
    if matrix[row_idx][col_idx] == symbol:
        center = True
    if row_idx - 1 >= 0 and matrix[row_idx-1][col_idx] == symbol:
        top = True
    if row_idx + 1 < len(matrix) and matrix[row_idx + 1][col_idx] == symbol:
        bot = True
    if col_idx - 1 >= 0 and matrix[row_idx][col_idx-1] == symbol:
        left = True
    if col_idx + 1 < len(matrix[row_idx]) and matrix[row_idx][col_idx+1] == symbol:
        right = True

    return top and left and right and bot and center

n = int(input())
matrices = []
for i in range(n):
    matrices.append([])
for idx in range(n):
    line = input().split('|')
    for i in range(n):
        matrices[i].append(line[i].split())



possible_starts = set()
possible_middle = set()
symbol_stars = {}
stars_sum = 0
for m_idx, matrix in enumerate(matrices):
    for row_idx in range(1, len(matrix)-1):
        row = matrix[row_idx]
        for col_idx in range(1, len(matrix[row_idx])-1):
            coords = (row_idx, col_idx)
            if coords in possible_middle:
                # test if we can complete the star
                symbol = matrices[m_idx-1][row_idx][col_idx]
                if matrix[row_idx][col_idx] == symbol:
                    # COMPLETED STAR
                    if symbol not in symbol_stars:
                        symbol_stars[symbol] = 0
                    symbol_stars[symbol] += 1
                    stars_sum += 1
                possible_middle.remove(coords)

            if coords in possible_starts:
                # test if the middle :)
                symbol = matrices[m_idx-1][row_idx][col_idx]
                if test_in_middle(matrix, row_idx, col_idx, symbol):
                    possible_middle.add(coords)
                possible_starts.remove(coords)
            possible_starts.add(coords)

print(stars_sum)
sorted_stars = sorted(symbol_stars.keys())
for key in sorted_stars:
    print('{symbol} -> {stars}'.format(symbol=key, stars=symbol_stars[key]))