import unittest
from unittest.mock import patch, MagicMock
import timeout_decorator

import server
from server import Player


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

if __name__ == '__main__':
    unittest.main()
