import pytest
from src.calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_addition(calculator):
    result = calculator.add(4, 6)
    assert result == 10


def test_division(calculator):
    result = calculator.divide(20, 4)
    assert result == 5.0


def test_division_by_zero(calculator):
    with pytest.raises(ValueError):
        calculator.divide(15, 0)


def test_initial_memory(calculator):
    assert calculator.get_memory() == 0


def test_store_in_memory(calculator):
    calculator.add_to_memory(8)
    assert calculator.get_memory() == 8


def test_reset_memory(calculator):
    calculator.add_to_memory(12)
    calculator.clear_memory()
    assert calculator.get_memory() == 0