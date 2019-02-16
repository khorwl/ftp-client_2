import unittest

from tools.helper import compute_download_percentage, from_string_to_command_and_args


class HelperUnitTests(unittest.TestCase):
    def test_compute_download_percentage__should_return_right_value(self):
        expected = 9

        actual = round(compute_download_percentage(64053, 5823))

        self.assertEqual(expected, actual)

    def test_compute_download_percentage__computing_with_zero__should_return_right_value(self):
        expected = None

        actual = compute_download_percentage(0, 5823)

        self.assertEqual(expected, actual)

    def test_from_string_to_command_and_args__should_return_right_value(self):
        str = "255.255.0.7 21"
        expected = server = ["255.255.0.7", "21"]

        actual = from_string_to_command_and_args(str)

        self.assertEqual(expected, actual)

    def test_from_string_to_command_and_args__command_without_args__should_return_right_value(self):
        str = "login"
        expected = ["login"]

        actual = from_string_to_command_and_args(str)

        self.assertEqual(expected, actual)

    def test_from_string_to_command_and_args__command_with_two_args__should_return_right_value(self):
        str = "command one two"
        expected = ["command", "one", "two"]

        actual = from_string_to_command_and_args(str)

        self.assertEqual(expected, actual)

    def test_from_string_to_command_and_args__with_wrong_arg__should_return_right_value(self):
        str = 12
        expected = None

        actual = from_string_to_command_and_args(str)

        self.assertEqual(expected, actual)
