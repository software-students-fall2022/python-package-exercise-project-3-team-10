import pytest
from src.converterpackageteam10 import number_converter

def test_decimal_to_binary():
    expected = '0b1010'
    actual = number_converter.convert_number("binary", 10)
    assert actual == expected, "Expected 10 to be equal to 0b1010!"

def test_binary_to_decimal():
    expected = 10
    actual = number_converter.convert_number("decimal", 0b1010)
    assert actual == expected, "Expected 0b1010 to be equal to 10!"

def test_decimal_to_octal():
    expected = '0o12'
    actual = number_converter.convert_number("octal", 10)
    assert actual == expected, "Expected 10 to be equal to 0o12!"

def test_octal_to_decimal():
    expected = 10
    actual = number_converter.convert_number("decimal", 0o12)
    assert actual == expected, "Expected 0o12 to be equal to 10!"

def test_decimal_to_hexadecimal():
    expected = '0xa'
    actual = number_converter.convert_number("hexadecimal", 10)
    assert actual == expected, "Expected 10 to be equal to 0xa!"

def test_hexadecimal_to_decimal():
    expected = 10
    actual = number_converter.convert_number("decimal", 0xa)
    assert actual == expected, "Expected 0xa to be equal to 10!"

def test_octal_to_binary():
    expected = '0b1010'
    actual = number_converter.convert_number("binary", 0o12)
    assert actual == expected, "Expected 0o12 to be equal to 0b1010!"

def test_binary_to_octal():
    expected = '0o12'
    actual = number_converter.convert_number("octal", 0b1010)
    assert actual == expected, "Expected 0b1010 to be equal to 0o12!"

def test_hexadecimal_to_binary():
    expected = '0b1010'
    actual = number_converter.convert_number("binary", 0xa)
    assert actual == expected, "Expected 0xa to be equal to 0b1010!"

def test_binary_to_hexadecimal():
    expected = '0xa'
    actual = number_converter.convert_number("hexadecimal", 0b1010)
    assert actual == expected, "Expected 0b1010 to be equal to 0xa!"

def test_hexadecimal_to_octal():
    expected = '0o12'
    actual = number_converter.convert_number("octal", 0xa)
    assert actual == expected, "Expected 0xa to be equal to 0o12!"

def test_octal_to_hexadecimal():
    expected = '0xa'
    actual = number_converter.convert_number("hexadecimal", 0o12)
    assert actual == expected, "Expected 0o12 to be equal to 0xa!"

def test_invalid_numeral_system():
    with pytest.raises(ValueError):
        number_converter.convert_number("senary", 10)

def test_invalid_number():
    with pytest.raises(ValueError):
        number_converter.convert_number("binary", "ten")