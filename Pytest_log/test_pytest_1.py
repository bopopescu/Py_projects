import pytest


# py.test pytest_1.py
# py.test -v -s pytest_1.py

@pytest.fixture()
def setUp():
    print("Once before every test_log")

def test_logA(setUp):
    print("Running test_logA")

def test_logB(setUp):
    print("Running test_logB")

