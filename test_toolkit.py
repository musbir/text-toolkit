import unittest

from toolkit import is_palindrome, slugify, word_count


class TestIsPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_palindrome_with_spaces_and_case(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))


class TestSlugify(unittest.TestCase):
    def test_basic_sentence(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_repeated_separators(self):
        self.assertEqual(slugify("foo   bar--baz"), "foo-bar-baz")

    def test_strips_leading_and_trailing_hyphens(self):
        self.assertEqual(slugify("--Trim Me--"), "trim-me")


class TestWordCount(unittest.TestCase):
    def test_basic_sentence(self):
        self.assertEqual(word_count("the quick brown fox"), 4)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)

    def test_extra_whitespace(self):
        self.assertEqual(word_count("  lots   of   space  "), 3)


if __name__ == "__main__":
    unittest.main()
