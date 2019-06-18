"""
file name should start with test
py.test filename.py
py.test somepath
py.test filename.py::test_method
-s print statement
-v verbose


"""
import pytest


# py.test pytest_1.py
# py.test -v -s pytest_1.py

@pytest.yield_fixture()
def setUp():
    print("Once before every test_log")
    yield
    print("Once After every test_log")

def test_logA(setUp):
    print("Running test_logA")

def test_logB(setUp):
    print("Running test_logB")

