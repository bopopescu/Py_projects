# python -m pytest -m set2
import pytest

@pytest.mark.set2
def test_file1_method1():
    x, y = 5, 6
    assert x+1 == y, "x + 1 == y failed"
    #assert x == y, "x==y failed"
    assert x == y, "test failed because x=" + str(x) + " y=" + str(y)

@pytest.mark.set2
def test_file1_method2():
    x, y = 5, 6
    assert x + 1 == y, "x + 1 == y Failed"