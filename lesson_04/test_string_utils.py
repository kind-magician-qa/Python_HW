import pytest
from string_utils import StringUtils


@pytest.mark.positive
@pytest.mark.parametrize("word,expected", [
    ("Skypro", "Skypro"),
    ("skyPro", "Skypro"),
    ("skyprO", "Skypro"),
    ("sky Pro", "Sky pro")
])
def test_capitalize_parametrized_positive(word, expected):
    s = StringUtils()
    assert s.capitalize(word) == expected


@pytest.mark.negative
@pytest.mark.parametrize("word, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_parametrized_negative(word, expected):
    s = StringUtils()
    assert s.capitalize(word) == expected


@pytest.mark.positive
@pytest.mark.parametrize("word, expected", [
    ("   Skypro", "Skypro"),
    ("  Sky  pro  ", "Sky  pro  "),
])
def test_trim_leading_spaces_parametrized_positive(word, expected):
    s = StringUtils()
    assert s.trim(word) == expected


@pytest.mark.negative
@pytest.mark.parametrize("word, expected", [
    ("Skypro", "Skypro"),
    ("", ""),
    ("   ", "")
])
def test_trim_leading_spaces_parametrized_negative(word, expected):
    s = StringUtils()
    assert s.trim(word) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string,symbol,expected", [
    ("Skypro", "S", True),
    ("Skypro", "p", True),
    ("Skypro", "o", True),
    ("Sky pro", " ", True),
    ("123 pro", "2", True),
    ("123 pro", "123", True),
])
def test_contains_parametrized_positive(string, symbol, expected):
    s = StringUtils()
    assert s.contains(string, symbol) is expected


@pytest.mark.negative
@pytest.mark.parametrize("string,symbol,expected", [
    ("Skypro", " ", False),
    ("Skypro", "1", False),
    ("Skypro", "s", False),
    ("Sky pro", "ss", False),
    ("123 pro", "0", False),
    ("123 pro", "1234", False),
])
def test_contains_parametrized_negative(string, symbol, expected):
    s = StringUtils()
    assert s.contains(string, symbol) is expected


@pytest.mark.positive
@pytest.mark.parametrize("string,symbol,expected", [
    ("Skypro", "pro", "Sky"),
    ("SkyPro", "k", "SyPro"),  # один символ
    ("SkyPro", "Pro", "Sky"),  # подстрока
    ("aaaa", "a", ""),  # все символы
    ("abcabc", "bc", "aa"),  # повторяющаяся подстрока
    ("Hello World", " ", "HelloWorld"),  # пробелы
])
def test_delete_symbol_parametrized_positive(string, symbol, expected):
    s = StringUtils()
    assert s.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "a", ""),
    ("SkyPro", "z", "SkyPro"),
    ("SkyPro", "", "SkyPro"),
])
def test_delete_symbol_negative(string, symbol, expected):
    s = StringUtils()
    assert s.delete_symbol(string, symbol) == expected