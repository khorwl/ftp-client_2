import unittest

from constants import len_progress_bar
from tools.get_progress_bar import compute_count_symbols_in_progress_bar, is_integer, get_progress_bar


class GetProgressBarUnitTests(unittest.TestCase):
    def test_compute_count_symbols_in_progress_bar__getting_by_100_percent__should_return_len_progress_bar(self):
        percent = 100
        expected = len_progress_bar

        actual = compute_count_symbols_in_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_compute_count_symbols_in_progress_bar__getting_by_50_percent__should_return_None(self):
        percent = 50
        expected = 25

        actual = compute_count_symbols_in_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_compute_count_symbols_in_progress_bar__getting_by_20_percent__should_return_5(self):
        percent = 20
        expected = 10

        actual = compute_count_symbols_in_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_compute_count_symbols_in_progress_bar__getting_by_200_percent__should_return_5(self):
        percent = 200
        expected = None

        actual = compute_count_symbols_in_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_compute_count_symbols_in_progress_bar__getting_by_minus20_percent__should_return_5(self):
        percent = -20
        expected = None

        actual = compute_count_symbols_in_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_compute_count_symbols_in_progress_bar__getting_by_11_percent__should_return_right_value(self):
        percent = 11
        expected = 6

        actual = compute_count_symbols_in_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_compute_count_symbols_in_progress_bar__getting_by_40_percent__should_return_10(self):
        percent = 40
        expected = 20

        actual = compute_count_symbols_in_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_is_integer__should_return_True(self):
        self.assertTrue(is_integer(11))
        self.assertTrue(is_integer(len_progress_bar))
        self.assertTrue(is_integer(float(92)))
        self.assertTrue(is_integer(4.0))

    def test_is_integer__should_return_False(self):
        self.assertFalse(is_integer(1.1))
        self.assertFalse(is_integer(len_progress_bar + 0.1))
        self.assertFalse(is_integer(9.2))
        self.assertFalse(is_integer(0.4))

    def test_get_progress_bar__getting_by_100_percent__should_return_right_value(self):
        expected = "[//////////////////////////////////////////////////]"
        percent = 100

        actual = get_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_get_progress_bar__getting_by_40_percent__should_return_right_value(self):
        expected = "[////////////////////..............................]"
        percent = 40

        actual = get_progress_bar(percent)

        self.assertEqual(expected, actual)

    def test_get_progress_bar__getting_by_11_percent__should_return_right_value(self):
        expected = "[//////............................................]"
        percent = 11

        actual = get_progress_bar(percent)

        self.assertEqual(expected, actual)