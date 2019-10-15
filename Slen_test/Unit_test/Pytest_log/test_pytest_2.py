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
# py.test will be out-dated, use python -m pytest -v -s


@pytest.yield_fixture()
def setUp():
    print("\nOnce before every test_log")
    yield
    print("\nOnce After every test_log")

def test_logA(setUp):
    print("Running test_logA")

def test_logB(setUp):
    print("Running test_logB")

