# text-toolkit

[![Tests](https://github.com/musbir/text-toolkit/actions/workflows/tests.yml/badge.svg)](https://github.com/musbir/text-toolkit/actions/workflows/tests.yml)

A small collection of pure Python text utility functions.

## Functions

- `is_palindrome(text)` — checks if text reads the same forwards and backwards
- `slugify(text)` — converts text into a lowercase, hyphen-separated slug
- `word_count(text)` — counts the number of words in text

## Usage

```python
from toolkit import is_palindrome, slugify, word_count

is_palindrome("A man a plan a canal Panama")  # True
slugify("Hello, World!")                       # "hello-world"
word_count("the quick brown fox")              # 4
```

## Testing

Run the test suite with:

```bash
python -m unittest discover
```
