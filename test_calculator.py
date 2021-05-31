from calculator import addition, division, multiplication, subtraction

def test_run_addition():
    result = addition(5, 2)
    assert result == 7

def test_run_subtraction():
    result = subtraction(5, 2)
    assert result == 3

def test_run_multiplication():
    result = multiplication(2, 2)
    assert result == 4

def test_run_division():
    result = division(10, 2)
    assert result == 5
