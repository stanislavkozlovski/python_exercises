from copy import deepcopy
from pprint import pprint
def aa():
    derive_banned_positions(None, None, None, None, None)

def derive_banned_positions(banned_x_y: set(), piece_type, piece, new_x, new_y) -> set():
    """
    In the case where a piece has another piece in its way,
    find the positions that piece is stopping us from getting to
     Example:
     Rook - X - Y - Rook - Z - L
     If we're the first Rook, the second Rook is stopping us from getting to Z and L
    """
    if piece_type == 'R':
        if new_x > piece[0]:
            # moved down
            for j in range(new_x + 1, 4):
                banned_x_y.add((j, new_y))
        elif new_x < piece[0]:
            # moved up
            for j in range(0, new_x):
                banned_x_y.add((j, new_y))
        elif new_y > piece[1]:
            # moved right
            for j in range(new_y + 1, 4):
                banned_x_y.add((new_x, j))
        elif new_y < piece[1]:
            # moved left
            for j in range(0, new_y):
                banned_x_y.add((new_x, j))
    elif piece_type == 'B':
        if new_x > piece[0] and new_y > piece[1]:
            # Diagonally down-right
            n_x, n_y = new_x + 1, new_y + 1
            while n_x < 4 and n_y < 4:
                banned_x_y.add((n_x, n_y))
                n_x += 1
                n_y += 1
        elif new_x > piece[0] and new_y < piece[1]:
            # Diagonally down-left
            n_x, n_y = new_x + 1, new_y - 1
            while n_x < 4 and n_y >= 0:
                banned_x_y.add((n_x, n_y))
                n_x += 1
                n_y -= 1
            pass
        elif new_x < piece[0] and new_y > piece[1]:
            # Diagonally upright
            n_x, n_y = new_x - 1, new_y + 1
            while n_x >= 0 and n_y < 4:
                banned_x_y.add((n_x, n_y))
                n_x -= 1
                n_y += 1
            pass
        elif new_x < piece[0] and new_y < piece[1]:
            # Diagonally upleft
            n_x, n_y = new_x - 1, new_y - 1
            while n_x >= 0 and n_y >= 0:
                banned_x_y.add((n_x, n_y))
                n_x -= 1
                n_y -= 1
    elif piece_type == 'Q':
        if new_x > piece[0] and new_y > piece[1]:
            # Diagonally down-right
            n_x, n_y = new_x + 1, new_y + 1
            while n_x < 4 and n_y < 4:
                banned_x_y.add((n_x, n_y))
                n_x += 1
                n_y += 1
        elif new_x > piece[0] and new_y < piece[1]:
            # Diagonally down-left
            n_x, n_y = new_x + 1, new_y - 1
            while n_x < 4 and n_y >= 0:
                banned_x_y.add((n_x, n_y))
                n_x += 1
                n_y -= 1
            pass
        elif new_x < piece[0] and new_y > piece[1]:
            # Diagonally upright
            n_x, n_y = new_x - 1, new_y + 1
            while n_x >= 0 and n_y < 4:
                banned_x_y.add((n_x, n_y))
                n_x -= 1
                n_y += 1
            pass
        elif new_x < piece[0] and new_y < piece[1]:
            # Diagonally upleft
            n_x, n_y = new_x - 1, new_y - 1
            while n_x >= 0 and n_y >= 0:
                banned_x_y.add((n_x, n_y))
                n_x -= 1
                n_y -= 1
        # -------------
        elif new_x > piece[0]:
            # moved down
            for j in range(new_x + 1, 4):
                banned_x_y.add((j, new_y))
        elif new_x < piece[0]:
            # moved up
            for j in range(0, new_x):
                banned_x_y.add((j, new_y))
        elif new_y > piece[1]:
            # moved right
            for j in range(new_y + 1, 4):
                banned_x_y.add((new_x, j))
        elif new_y < piece[1]:
            # moved left
            for j in range(0, new_y):
                banned_x_y.add((new_x, j))


def build_board():
    board = []

    for i in range(4):
        board.append([None] * 4)

    return board

ROWS = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3
}
POSSIBLE_MOVES = {
    'N': [(-2, -1), (-2, 1),
          (-1, -2), (1, -2),
          (2, -1), (2, 1),
          (-1, 2), (1, 2)],
    'R': [(0, 1), (0, 2), (0, 3),
          (0, -1), (0, -2), (0, -3),
          (1, 0), (2, 0), (3, 0),
          (-1, 0), (-2, 0), (-3, 0)],
    'B': [(1, 1), (2, 2), (3, 3),
          (-1, 1), (-2, 2), (-3, 3),
          (1, -1), (2, -2), (3, -3),
          (-1, -1), (-2, -2), (-3, -3)],
    'Q': [(1, 1), (2, 2), (3, 3),
          (-1, 1), (-2, 2), (-3, 3),
          (1, -1), (2, -2), (3, -3),
          (-1, -1), (-2, -2), (-3, -3),
          (0, 1), (0, 2), (0, 3),
          (0, -1), (0, -2), (0, -3),
          (1, 0), (2, 0), (3, 0),
          (-1, 0), (-2, 0), (-3, 0)]
}


def recurse(board, black_pieces, white_pieces, max_op):
    has_won = False

    def __recurse(board, black_pieces, white_pieces, op):
        nonlocal has_won
        if op == max_op or has_won:
            return

        if op % 2 == 0:
            # WHITE MOVE
            w_pieces = deepcopy(white_pieces)  # deepcopy of the set to modify it

            for w_piece in white_pieces:
                """
                Try to find an optimal move which results in a win for white
                """
                white_piece_type = board[w_piece[0]][w_piece[1]]
                w_pieces.remove(w_piece)
                banned_x_y = set()

                for x, y in POSSIBLE_MOVES[white_piece_type]:
                    new_x, new_y = w_piece[0] + x, w_piece[1] + y
                    new_position = (new_x, new_y)
                    if new_position in w_pieces:
                        # A white piece is in our way
                        derive_banned_positions(banned_x_y=banned_x_y, piece_type=white_piece_type,
                                                piece=w_piece, new_x=new_x, new_y=new_y)
                        continue
                    valid_move = new_position not in w_pieces and 4 > new_x >= 0 <= new_y < 4 and new_position not in banned_x_y

                    if valid_move:
                        old_piece = board[new_x][new_y]
                        if old_piece == 'Q':
                            # has_won = True
                            if op == 0:
                                has_won = True
                            return True
                        elif old_piece is not None and white_piece_type != 'N':
                            derive_banned_positions(banned_x_y=banned_x_y, piece_type=white_piece_type,
                                                    piece=w_piece, new_x=new_x, new_y=new_y)

                        w_pieces.add(new_position)
                        board[w_piece[0]][w_piece[1]] = None
                        board[new_x][new_y] = white_piece_type

                        if new_position in black_pieces:
                            black_pieces.remove(new_position)
                            # RECURSE
                            has_killed_queen = __recurse(board, black_pieces=black_pieces, white_pieces=w_pieces, op=op + 1)
                            black_pieces.add(new_position)
                        else:
                            # RECURSE
                            has_killed_queen = __recurse(board, black_pieces=black_pieces, white_pieces=w_pieces, op=op + 1)

                        # Backtrace
                        board[new_x][new_y] = old_piece
                        board[w_piece[0]][w_piece[1]] = white_piece_type
                        w_pieces.remove(new_position)
                        """
                        Since we always take the most optimal move, if there is a move that kills black's queen, we take it
                        """
                        if has_killed_queen:
                            return has_killed_queen

                w_pieces.add(w_piece)
        else:
            # BLACK MOVE
            b_pieces = deepcopy(black_pieces)  # deepcopy of the set to modify it
            results = []
            for b_piece in black_pieces:
                b_x, b_y = b_piece
                black_piece_type = board[b_x][b_y]
                b_pieces.remove(b_piece)
                banned_x_y = set()
                for x, y in POSSIBLE_MOVES[black_piece_type]:
                    new_x = b_x + x
                    new_y = b_y + y
                    new_pos = (new_x, new_y)
                    if new_pos in b_pieces:
                        # a black piece is in our way
                        derive_banned_positions(banned_x_y=banned_x_y, piece_type=black_piece_type,
                                                piece=b_piece, new_x=new_x, new_y=new_y)
                        continue
                    valid_move = new_pos not in b_pieces and 4 > new_x >= 0 <= new_y < 4 and new_pos not in banned_x_y

                    if valid_move:
                        old_piece = board[new_x][new_y]

                        if old_piece == 'Q':
                            # LOST
                            return
                        elif old_piece is not None and black_piece_type != 'N':
                            derive_banned_positions(banned_x_y=banned_x_y, piece_type=black_piece_type,
                                                    piece=b_piece, new_x=new_x, new_y=new_y)

                        board[b_x][b_y] = None
                        board[new_x][new_y] = black_piece_type
                        b_pieces.add(new_pos)

                        if new_pos in white_pieces:
                            white_pieces.remove(new_pos)
                            results.append(__recurse(board, black_pieces=b_pieces, white_pieces=white_pieces, op=op + 1))
                            white_pieces.add(new_pos)
                        else:
                            results.append(__recurse(board, black_pieces=b_pieces, white_pieces=white_pieces, op=op + 1))

                        b_pieces.remove(new_pos)
                        board[new_x][new_y] = old_piece
                        board[b_x][b_y] = black_piece_type
                b_pieces.add(b_piece)
            if all(results):
                if op == 1:
                    has_won = True
                return True

    __recurse(board, black_pieces, white_pieces, 0)
    return has_won


def main():
    test_case_count = int(input())

    for _ in range(test_case_count):
        board = build_board()

        w, b, m = [int(p) for p in input().split()]
        if m % 2 == 0:
            m -= 1
        # white pieces
        white_pieces = set()
        for _ in range(w):
            piece, col, row = input().split()
            col = ROWS[col]
            row = abs(int(row) - 4)
            white_pieces.add((row, col))
            board[row][col] = piece
        # black pieces
        black_pieces = set()
        for _ in range(b):
            piece, col, row = input().split()
            col = ROWS[col]
            row = abs(int(row) - 4)
            black_pieces.add((row, col))
            board[row][col] = piece

        result = recurse(board, black_pieces, white_pieces, m)
        print('YES' if result else 'NO')


if __name__ == '__main__':
    main()
