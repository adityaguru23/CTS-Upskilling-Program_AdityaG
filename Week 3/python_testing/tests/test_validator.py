import pytest
from src.validator import valdiate_registration_password


def test_valid_password():
    assert valdiate_registration_password("PyTest@2026")


def test_password_with_min_length():
    assert valdiate_registration_password("aB1!dfjh")


def test_empty_password():
    with pytest.raises(ValueError):
        valdiate_registration_password("")


def test_short_password():
    with pytest.raises(ValueError):
        valdiate_registration_password("Short1!")


def test_password_with_max_length():
    assert valdiate_registration_password("aB1!dfjhfi2385839f")


def test_long_password():
    with pytest.raises(ValueError):
        valdiate_registration_password("idsjoidjfpikdpskfpdkfspdofkpsokdpfk")


def test_password_has_letters_and_digits():
    assert valdiate_registration_password("Pass@1234")


def test_password_without_digit():
    with pytest.raises(ValueError):
        valdiate_registration_password("HelloWorld")


def test_password_without_uppercase():
    with pytest.raises(ValueError):
        valdiate_registration_password("secure@123")


def test_password_without_lowercase():
    with pytest.raises(ValueError):
        valdiate_registration_password("SECURE@123")