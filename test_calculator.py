from calculator import Calculator
def test_add():
    calc = Calculator()
    assert calc.add(1, 2) == 3
    assert calc.add(0, 0) == 0

def test_substract():
    calc = Calculator()
    assert calc.substract(3, 2) == 1
    assert calc.substract(5, 5) == 0

def test_multiplication():
    calc = Calculator()
    assert calc.multiplication(2, 3) == 6
    assert calc.multiplication(4, 0) == 0
def test_division():
    calc = Calculator()
    assert calc.division(6, 3) == 2
    assert calc.division(5, 2) == 2.5
    try:
        calc.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"