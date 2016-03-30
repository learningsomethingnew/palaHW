import unittest

from palindrome import is_palindrome
from palindrome import is_palindrome_iterative

class TestPalindrome(unittest.TestCase):
    def test_even_numbers(self):
        self.assertTrue(is_palindrome('toot'))
        self.assertTrue(is_palindrome('toot'))

    def test_odd_numbers(self):
        self.assertTrue(is_palindrome('tot'))
        self.assertTrue(is_palindrome_iterative('tot'))

    def test_simple_values(self):
        self.assertTrue(is_palindrome('stunt nuts'))
        self.assertTrue(is_palindrome_iterative('stunt nuts'))

    def test_complete_sentences(self):
        self.assertTrue(is_palindrome('Lisa Bonet ate no basil.'))
        self.assertTrue(is_palindrome_iterative('Lisa Bonet ate no basil.'))

    def test_complex_sentences(self):
        self.assertTrue(is_palindrome('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!'))
        self.assertTrue(is_palindrome_iterative('A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal: Panama!'))

    def test_multiple_sentences(self):
        self.assertTrue(is_palindrome('Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.'))
        self.assertTrue(is_palindrome_iterative('Doc, note, I dissent. A fast never prevents a fatness. I diet on cod.'))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome('i am not a palindrome'))
        self.assertFalse(is_palindrome_iterative('i am not a palindrome'))


if __name__ == '__main__':
    unittest.main()