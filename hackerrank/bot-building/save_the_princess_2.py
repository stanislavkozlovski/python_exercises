"""
In this version of "Bot saves princess", Princess Peach and bot's position are randomly set. Can you save the princess?

Task

Complete the function nextMove which takes in 4 parameters - an integer N, integers r and c indicating the row & column position of the bot and the character array grid - and outputs the next move the bot makes to rescue the princess.

Input Format

The first line of the input is N (<100), the size of the board (NxN). The second line of the input contains two space separated integers, which is the position of the bot.

Grid is indexed using Matrix Convention

The position of the princess is indicated by the character 'p' and the position of the bot is indicated by the character 'm' and each cell is denoted by '-' (ascii value: 45).

Output Format

Output only the next move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN

Sample Input

5
2 3
-----
-----
p--m-
-----
-----
Sample Output

LEFT
Resultant State

-----
-----
p-m--
-----
-----
Explanation

As you can see, bot is one step closer to the princess.

Scoring
Your score for every testcase would be (NxN minus number of moves made to rescue the princess)/10 where N is the size of the grid (5x5 in the sample testcase). Maximum score is 17.5
"""


def main():
    rows = int(input())
    matrix = []
    princess_row, princess_col = [int(coord) for coord in input().split()]
    bot_row, bot_col = 0, 0
    # read input
    for row_idx in range(rows):
        new_row = list(input())
        if 'p' in new_row:
            princess_row, princess_col = row_idx, new_row.index('p')
        if 'm' in new_row:
            bot_row, bot_col = row_idx, new_row.index('m')
        matrix.append(new_row)
    display_path_to_princess(bot_row, bot_col, princess_row, princess_col, matrix)


def display_path_to_princess(bot_row, bot_col, princess_row, princess_col, matrix):
    last_move = ''
    while bot_row != princess_row:
        if bot_row > princess_row:
            bot_row -= 1
            last_move = 'UP'
        else:
            bot_row += 1
            last_move = 'DOWN'

    while bot_col != princess_col:
        if bot_col > princess_col:
            bot_col -= 1
            last_move = 'LEFT'
        else:
            bot_col += 1
            last_move = 'RIGHT'
    print(last_move)

if __name__ == '__main__':
    main()