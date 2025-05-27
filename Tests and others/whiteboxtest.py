import unittest
from IsValidPassword import is_valid_length

class TestIsValidLength(unittest.TestCase):
    def test_too_short(self):
        self.assertFalse(is_valid_length("abc"))  # length 3 < 6

    def test_exact_length(self):
        self.assertTrue(is_valid_length("abcdef"))  # length 6 == 6

    def test_longer_length(self):
        self.assertTrue(is_valid_length("abcdefgh"))  # length 8 > 6

if __name__ == '__main__':
    unittest.main()