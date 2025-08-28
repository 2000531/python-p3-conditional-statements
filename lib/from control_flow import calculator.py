from control_flow import calculator
import io
import sys

# Python


class TestCalculator:
    def test_returns_sum_if_plus(self):
        assert calculator("+", 1, 2) == 3
        assert calculator("+", 5, 7) == 12
        assert calculator("+", 9, 90) == 99

    def test_returns_difference_if_minus(self):
        assert calculator("-", 1, 2) == -1
        assert calculator("-", 7, 5) == 2
        assert calculator("-", 9, 9) == 0

    def test_returns_product_if_times(self):
        assert calculator("*", 1, 2) == 2
        assert calculator("*", 5, 7) == 35
        assert calculator("*", 9, 10) == 90

    def test_returns_quotient_if_divided_by(self):
        assert calculator("/", 1, 1) == 1
        assert calculator("/", 14, 7) == 2
        assert calculator("/", 90, 9) == 10

    def test_prints_invalid_returns_none_if_invalid(self):
        captured_out = io.StringIO()
        sys.stdout = captured_out
        assert calculator('a', 1, 2) is None
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "Invalid operation!\n"