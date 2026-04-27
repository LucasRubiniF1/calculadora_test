import pytest
from app.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# ── Casos exitosos ──────────────────────────────────────────────────────────

class TestAdd:
    def test_add_positive_numbers(self, calc):
        assert calc.add(3, 5) == 8

    def test_add_negative_numbers(self, calc):
        assert calc.add(-2, -3) == -5

    def test_add_floats(self, calc):
        assert calc.add(1.5, 2.5) == pytest.approx(4.0)


class TestSubtract:
    def test_subtract_positive_numbers(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_subtract_resulting_negative(self, calc):
        assert calc.subtract(3, 7) == -4


class TestMultiply:
    def test_multiply_positive_numbers(self, calc):
        assert calc.multiply(4, 5) == 20

    def test_multiply_by_negative(self, calc):
        assert calc.multiply(6, -3) == -18


class TestDivide:
    def test_divide_positive_numbers(self, calc):
        assert calc.divide(10, 2) == pytest.approx(5.0)

    def test_divide_resulting_float(self, calc):
        assert calc.divide(7, 2) == pytest.approx(3.5)


# ── Casos de error ──────────────────────────────────────────────────────────

class TestDivideErrors:
    def test_divide_by_zero_raises_value_error(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_divide_negative_by_zero_raises_value_error(self, calc):
        with pytest.raises(ValueError):
            calc.divide(-5, 0)


# ── Casos borde (edge cases) ────────────────────────────────────────────────

class TestEdgeCases:
    def test_add_zero_is_identity(self, calc):
        assert calc.add(99, 0) == 99

    def test_multiply_by_zero_returns_zero(self, calc):
        assert calc.multiply(12345, 0) == 0

    def test_divide_zero_by_number_returns_zero(self, calc):
        assert calc.divide(0, 5) == pytest.approx(0.0)

    def test_subtract_same_numbers_returns_zero(self, calc):
        assert calc.subtract(42, 42) == 0

    def test_operations_with_very_large_numbers(self, calc):
        assert calc.add(10**18, 1) == 10**18 + 1

    def test_divide_results_in_repeating_decimal(self, calc):
        # 1/3 no es exactamente representable en punto flotante
        assert calc.divide(1, 3) == pytest.approx(0.3333333333333333)
