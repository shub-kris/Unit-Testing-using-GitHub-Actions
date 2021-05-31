from calculator import addition, subtraction

def test_run_addition():
    result = addition(5, 2)
    assert result == 7

def test_run_subtraction():
    result = subtraction(5, 2)
    assert result == 3

