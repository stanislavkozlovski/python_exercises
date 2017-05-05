require 'set'

# Holds pairs of numbers, representing the X and Y values
#                         we should add/subtract to go in the given direction of a 2D Matrix
VALID_DIRECTIONS = Hash.new
VALID_DIRECTIONS['LEFT'] = [0, -1]
VALID_DIRECTIONS['RIGHT'] = [0, 1]
VALID_DIRECTIONS['UP'] = [-1, 0]
VALID_DIRECTIONS['UPRIGHT'] = [-1, 1]
VALID_DIRECTIONS['UPLEFT'] = [-1, -1]
VALID_DIRECTIONS['DOWNRIGHT'] = [1, 1]
VALID_DIRECTIONS['DOWNLEFT'] = [1, -1]
VALID_DIRECTIONS['DOWN'] = [1, 0]

# holds pairs of directions, representing the two directions we need to go in to traverse a whole tic tac toe row
VALID_ROWS = Hash.new
VALID_ROWS['HORIZONTAL'] = [VALID_DIRECTIONS['LEFT'], VALID_DIRECTIONS['RIGHT']]
VALID_ROWS['VERTICAL'] = [VALID_DIRECTIONS['UP'], VALID_DIRECTIONS['DOWN']]
VALID_ROWS['LEFT_DIAGONAL'] = [VALID_DIRECTIONS['UPLEFT'], VALID_DIRECTIONS['DOWNRIGHT']]
VALID_ROWS['RIGHT_DIAGONAL'] = [VALID_DIRECTIONS['UPRIGHT'], VALID_DIRECTIONS['DOWNLEFT']]

TIC_TAC_TOE_SYMBOLS = ['O', 'X', 'A', 'R', "V", "S", "E", "Q"]

class TicTacToe
  def initialize(players, board_x_size, board_y_size, needed_symbols)
    @players = players
    @board_x_size = board_x_size
    @board_y_size = board_y_size
    @needed_symbols = needed_symbols

    @board = build_board
    puts @board.size
    @empty_positions = find_empty_positions

    @active_player_idx = 0
    @game_has_ended = false
    @max_x = board_x_size
    @max_y = board_y_size
    @winner = nil
    set_player_symbols
  end

  def build_board
    Array.new(@board_x_size) {Array.new(@board_y_size, '[ ]')}
  end

  # Set the symbols of all the players
  def set_player_symbols
    @players.each_with_index do |player, idx|
      player.set_symbol(TIC_TAC_TOE_SYMBOLS[idx])
    end
  end

  def get_player_turn
    @active_player_idx
  end

  def get_winner
    @winner
  end

  #  Passes the turn to the next player
  def pass_player_turn
    @active_player_idx += 1
    if @active_player_idx == @players.length
      @active_player_idx = 0
    end
  end

  # Iterates through the board and returns a set of tuples, representing all the empty positions on the board
  def find_empty_positions
    empty_positions = Set.new
    (0..@board.size-1).each {|i|
      (0..@board[i].count-1).each {|j|
        if @board[i][j] == '[ ]'
          empty_positions.add([i, j])
        end
      }
    }
    empty_positions
  end

  def is_valid_board_size(x, y, needed_symbols)
    not (x <= 0 or y <= 0 or needed_symbols <= 0 or needed_symbols > [x,y].min )
  end

  # returns a string representation of the board
  def get_board_state
    board_repr = []

    for row in @board
      board_repr.push(row.reject(&:empty?).join(''))
    end

    board_repr.reject(&:empty?).join("\n")
  end

  def get_empty_positions
    return @empty_positions
  end

  def get_active_player_idx
    @active_player_idx
  end

  def is_free_position(x, y)
    0 <= x and x < @max_x and 0 <= y and y < @max_y and @board[x][y] == '[ ]'
  end

  def move_position(x, y)
    unless is_free_position(x, y)

    end
    unless @game_has_ended

    end

    active_player = @players[@active_player_idx]
    @board[x][y] = '[' + active_player.get_symbol + ']'
    @empty_positions.delete([x, y])
  end

  def run_turn(x, y)
    move_position(x, y)
    check_game_end(x, y)
    pass_player_turn
  end

  # checks if a winning move has been made
  def check_game_end(x, y)
    if @board[x][y] == '[ ]'
      return false
    end

    VALID_ROWS.each do |_, directions|
      direction_one, direction_two = *directions
      rows_symbol_count = get_cons_sym_count(x, y, direction_one) + get_cons_sym_count(x, y, direction_two) + 1

      if rows_symbol_count == @needed_symbols
        @game_has_ended = true
        @winner = @players[@active_player_idx]
        return true
      end

      if @empty_positions.length == 0  # This is a stalemate
        @game_has_ended = true
        @winner = nil
        return true
      end
    end

    false
  end

  def has_ended
    @game_has_ended
  end

  def get_cons_sym_count(x, y, direction)
    dir_x, dir_y = *direction
    original_symbol = @board[x][y]
    symbol_count = 0
    curr_x = x + dir_x
    curr_y = y + dir_y

    while 0 <= curr_x and curr_x < @max_x and 0 <= curr_y and curr_y < @max_y and @board[curr_x][curr_y] == original_symbol
      symbol_count += 1
      curr_x += dir_x
      curr_y += dir_y
    end

    symbol_count
  end

  private :build_board, :find_empty_positions
end

puts 'tank'
ttt = TicTacToe.new([], 5, 5, 2)
puts ttt.get_board_state