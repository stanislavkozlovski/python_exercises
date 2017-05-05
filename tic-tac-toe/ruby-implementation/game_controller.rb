require_relative 'player'
require_relative 'tic_tac_toe'

class InvalidInputError < StandardError
end


class GameController
  def initialize(player_count, board_x_size, board_y_size, needed_symbols)
    # TODO: Validate  via static method
    @players = Array.new
    (0..player_count-1).each {|_|
      @players.push(Player.new)
    }
    @board_x_size = board_x_size
    @board_y_size = board_y_size
    @needed_symbols = needed_symbols
  end

  def start_game
    game = TicTacToe.new(@players, @board_x_size, @board_y_size, @needed_symbols)

    puts 'The game has started!'

    while true
      puts game.get_board_state

      puts 'Player #' + game.instance_variable_get(:@active_player_idx).to_s + ' please choose a position to move.'

      puts 'Valid positions: '
      for pos in game.get_empty_positions
        puts '(' + pos[0].to_s + ', ' + pos[1].to_s + ')'
      end

      # try to parse the player input into coordinates and validate them
      begin
        x, y = parse_player_position(read_player_input)
        is_valid_position = game.is_free_position(x, y)
        puts is_valid_position
        unless is_valid_position
          puts 'The chosen position is taken!'
          next
        end
      rescue ArgumentError
        next  # skip the input and try to read it again
      end

      game_has_ended = handle_game_turn(game, x, y)

      if game_has_ended
        return
      end
    end
  end


# returns a boolean indicating if the game has ended
def handle_game_turn(game, x, y)
  game.run_turn(x, y)

  if game.has_ended
    if game.get_winner.nil?
      puts 'The game has ended in a stalemate!'
    else
      puts 'Player #' + game.get_active_player_idx.to_s + ' has won the game!'
      puts 'Other players, you have lost.'
    end
  end

  return game.has_ended
end

  def read_player_input
    gets.chomp
  end

  # receives a string as input and tries to parse it into a list of two coordinates - x and y
  # i.e parse("0 1") -> [0, 1]
  def parse_player_position(input)
    x, y = -1, -1
    begin
      x,y = *input.split.map { |a| Integer(a) }
    rescue ArgumentError
      puts 'Invalid input, could not parse it to X,Y coordinates!'
      raise InvalidInputError
    end

    [x, y]
  end
end

gc = GameController.new(2, 3, 3, 3)
gc.start_game