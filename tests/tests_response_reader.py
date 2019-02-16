import unittest

from tools.response_reader import is_code


class ResponseReaderUnitTests(unittest.TestCase):
    def test_is_code__should_return_true(self):
        self.assertTrue(is_code("102"))
        self.assertTrue(is_code("505"))
        self.assertTrue(is_code("404"))
        self.assertTrue(is_code("216"))

    def test_is_code__number_out_of_range__should_return_false(self):
        self.assertFalse(is_code("001"))
        self.assertFalse(is_code("099"))
        self.assertFalse(is_code("600"))
        self.assertFalse(is_code("601"))
        self.assertFalse(is_code("1000"))

    def test_is_code__with_not_number_arg__should_return_false(self):
        self.assertFalse(is_code("cat"))
        self.assertFalse(is_code("01l"))
        self.assertFalse(is_code("cod"))

