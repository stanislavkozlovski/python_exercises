import unittest
from unittest.mock import patch, MagicMock
import timeout_decorator

import server
from server import Player, TicTacToe


class TestError(Exception):
    """ Custom Exception type for testing """
    pass


class PlayerTests(unittest.TestCase):
    @patch('server.select.select')
    def test_receive_message_blocks_until_input_is_given(self, select_mock):
        select_mock.return_value = [None, None, None]

        @timeout_decorator.timeout(1, timeout_exception=TestError)
        def call_receive_message():
            Player(None).receive_message()

        try:
            call_receive_message()
            self.fail("Should have timed out")
        except TestError:
            pass


    @staticmethod
    def _select_mock(*args):
        """
        Mock the function with
            a generator to simulate the continued function call in the while loop"""
        none_value = [None, None, None]
        for i in [none_value, none_value, [True, True, True]]:
            yield i

    def test_receive_message_returns_message_after_iterations(self):
        """
        Assert that the select function is called multiple times
        and when it has received a signal - returns the message
        """
        server.select.select = self._select_mock
        recv_mock = MagicMock()
        recv_mock.return_value = "Message"
        connection_mock = MagicMock(recv=recv_mock)

        player = Player(connection_mock)
        received_message = player.receive_message()

        connection_mock.recv.assert_called_once()
        self.assertEqual(received_message, "Message")

    def test_send_message_encodes_msg_and_sends_it(self):
        message = "Hello :)"
        connection_mock = MagicMock(send=MagicMock())
        expected_send_args = bytes(message, 'utf-8')

        Player(connection_mock).send_message(message)

        connection_mock.send.assert_called_once_with(expected_send_args)

    def test_equals(self):
        """ The equals dunder should compare by the only unique thing
                per player - its connection """
        self.assertEqual(Player(1), Player(1))
        self.assertNotEqual(Player(1), Player(2))


class TicTacToeTests(unittest.TestCase):
    @patch('server.TicTacToe._build_board')
    @patch('server.TicTacToe.set_player_symbols')
    @patch('server.TicTacToe._get_empty_positions')
    @patch('server.TicTacToe.is_valid_board_size')
    def test_init(self, valid_board_size_mock, empty_positions_mock, set_player_symbols_mock, build_board_mock):
        """
        The TicTacToe init should call the
            is_valid_board_size, _build_board(), _get_empty_positions() and set_player_symbols() functions
            and assign them to the appropriate values
        """
        build_board_mock.return_value = 'The board'
        empty_positions_mock.return_value = "Empty positions"

        ttt = TicTacToe([1], board_x_size="X", board_y_size="Y", needed_symbols="Symbols")

        valid_board_size_mock.assert_called_once_with("X", "Y", "Symbols")
        empty_positions_mock.assert_called_once_with()
        self.assertEqual(ttt.empty_positions, "Empty positions")
        build_board_mock.assert_called_once_with("X", "Y")
        self.assertEqual(ttt.board, 'The board')
        set_player_symbols_mock.assert_called_once()

    @patch('server.TicTacToe.is_valid_board_size')
    def test_init_raises_exception_on_invalid_board_size(self, is_valid_mock):
        is_valid_mock.return_value = False

        with self.assertRaises(Exception):
            TicTacToe(None)

    @patch('server.randint')
    def test_init_assigns_random_player_index(self, randint_mock):
        players = [MagicMock(),MagicMock(),MagicMock(),MagicMock(),MagicMock(),MagicMock(),MagicMock()]
        randint_mock.return_value = 'random'

        ttt = TicTacToe(players=players)

        randint_mock.assert_called_once_with(0, len(players)-1)
        self.assertEqual(ttt._active_player_idx, 'random')

    def test_set_player_symbols_sets_all_symbols(self):
        symbols = ['1', '2', '3']
        server.TIC_TAC_TOE_SYMBOLS = symbols
        players = [MagicMock(name="1", set_symbol=MagicMock()), MagicMock(name="2", set_symbol=MagicMock()),
                   MagicMock(name="3", set_symbol=MagicMock())]

        ttt = TicTacToe(players=players)
        ttt.set_player_symbols()

        # assert that the set_symbols was called with the correct args
        for idx, player in enumerate(players):
            # Should be called with the appropriate symbols in order
            player.set_symbol.assert_called_with(symbols[idx])

    def test_pass_player_turn_correctly_passes_turn(self):
        """ Assert that it does goes back to the first player once it goes out of range"""
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])
        ttt._active_player_idx = 0

        for i in range(15):
            correct_idx = i % len(ttt.players)
            self.assertEqual(ttt._active_player_idx, correct_idx)
            ttt.pass_player_turn()

    def test_get_player_raises_exception_on_invalid_idx(self):
        """ That function should never be called with an invalid idx"""
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])

        with self.assertRaises(Exception):
            ttt.get_player(-1)
        with self.assertRaises(Exception):
            ttt.get_player(12)

    def test_build_board_builds_matrix(self):
        x_size, y_size = 4, 4
        expected_board = [
            ['[ ]', '[ ]', '[ ]', '[ ]'],
            ['[ ]', '[ ]', '[ ]', '[ ]'],
            ['[ ]', '[ ]', '[ ]', '[ ]'],
            ['[ ]', '[ ]', '[ ]', '[ ]']
        ]

        self.assertEqual(TicTacToe._build_board(x_size, y_size), expected_board)

    def test_get_empty_positions(self):
        sample_board = [
            ['[ ]', '[ ]', '[X]', '[X]'],
            ['[X]', '[X]', '[X]', '[ ]']
        ]
        expected_empty_positions = {(0,0), (0,1), (1, 3)}

        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])
        ttt.board = sample_board

        self.assertEqual(ttt._get_empty_positions(), expected_empty_positions)

    def test_is_valid_board_size_validates_xy_size(self):
        """ the is_valid_board_size should validate the x, y_size of the board"""
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=0, y_size=1, needed_symbols=1))
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=-1, y_size=1, needed_symbols=1))
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=2, y_size=0, needed_symbols=1))
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=2, y_size=-1, needed_symbols=1))

    def test_is_valid_board_size_validates_needed_symbols(self):
        """ The needed symbols cannot be 0, negative
        or more than what you would be able to achieve with the given dimensions"""
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=2, y_size=2, needed_symbols=3))
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=2, y_size=2, needed_symbols=0))
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=2, y_size=2, needed_symbols=-1))
        self.assertFalse(TicTacToe.is_valid_board_size(x_size=4, y_size=3, needed_symbols=4))

    def test_get_board_state_returns_string_repr_of_board(self):
        sample_board = [['[X]', '[O]'], ['[X]', '[O]']]
        expected_repr = '[X][O]\n[X][O]'

        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])
        ttt.board = sample_board

        self.assertEqual(ttt.get_board_state(), expected_repr)

    def test_is_free_positions_validates_properly(self):
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])

        self.assertFalse(ttt.is_free_position(-1, 1))
        self.assertFalse(ttt.is_free_position(2222, 1))
        self.assertFalse(ttt.is_free_position(1, -1))
        self.assertFalse(ttt.is_free_position(1, 2222))
        self.assertTrue(ttt.is_free_position(0, 0))
        ttt.board[0][0] = '[O]'
        self.assertFalse(ttt.is_free_position(0, 0))

    @patch('server.TicTacToe.is_free_position')
    def test_move_position_raises_exception_on_invalid_coords(self, is_free_mock):
        is_free_mock.return_value = False

        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])

        with self.assertRaises(Exception):
            ttt.move_position((0, 1))
        is_free_mock.assert_called_once_with(0, 1)

    def test_move_position_raises_exception_on_game_end(self):
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])
        ttt._game_has_ended = True

        with self.assertRaises(Exception):
            ttt.move_position(0, 1)

    def test_move_position_adds_active_player_symbol_to_position_and_passes_turn(self):
        active_player_mock = MagicMock(symbol='X')
        ttt = TicTacToe(players=[active_player_mock, MagicMock(), MagicMock()])
        ttt._active_player_idx = 0

        self.assertEqual(ttt.board[0][0], '[ ]')
        self.assertIn((0, 0), ttt.empty_positions)
        ttt.move_position((0, 0))

        self.assertNotIn((0, 0), ttt.empty_positions)
        self.assertEqual(ttt.board[0][0], '[X]')

    @patch('server.TicTacToe.check_game_end')
    @patch('server.TicTacToe.move_position')
    @patch('server.TicTacToe.pass_player_turn')
    def test_run_turn(self, pass_mock, move_mock, check_mock):
        """
        The run_turn function should move the position of a player,
        check if the game has ended and pass the turn
        """
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])
        ttt.run_turn((0, 1))

        pass_mock.assert_called_once()
        move_mock.assert_called_once_with((0, 1))
        check_mock.assert_called_once_with(0, 1)

    def test_check_game_end_returns_false_on_no_symbols(self):
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])
        ttt.check_game_end(0, 0)
        self.assertFalse(ttt._game_has_ended)

    def test_check_game_end_ends_game_on_stalemate(self):
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()])
        ttt.empty_positions = set()  # no more moves
        ttt.board[0][0] = '[X]'
        ttt.check_game_end(0, 0)

        self.assertTrue(ttt._game_has_ended)
        self.assertIsNone(ttt.winner)

    def test_check_game_end_finds_win(self):
        sample_board = [
            ['[R]', '[R]', '[X]'],
            ['[R]', '[X]', '[O]'],
            ['[X]', '[X]', '[O]']
        ]
        ttt = TicTacToe(players=[MagicMock(), MagicMock(), MagicMock()], needed_symbols=3)
        ttt.board = sample_board
        # the active player has placed a X on 0,2 and as such, won the game
        result = ttt.check_game_end(0, 2)

        self.assertTrue(result)
        self.assertTrue(ttt._game_has_ended)
        self.assertEqual(ttt.winner, ttt.players[ttt._active_player_idx])


if __name__ == '__main__':
    unittest.main()
