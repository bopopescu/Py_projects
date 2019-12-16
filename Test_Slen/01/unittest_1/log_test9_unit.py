import unittest


class Car(object):
  def __init__(self, make, model):
    self.make = make
    self.model = make  # Copy and paste error: should be model.
    self.has_seats = True
    self.wheel_count = 3  # Typo: should be 4.


class CarTest(unittest.TestCase):
  def setUp(self):
    self.verificationErrors = []

  def tearDown(self):
    self.assertEqual([], self.verificationErrors)

  def test_init(self):
    make = "Ford"
    model = "Model T"
    car = Car(make=make, model=model)
    try:
      self.assertEqual(car.make, make)
    except AssertionError, e:
      self.verificationErrors.append(str(e))
    try:
      self.assertEqual(car.model, model)  # Failure!
    except AssertionError, e:
      self.verificationErrors.append(str(e))
    try:
      self.assertTrue(car.has_seats)
    except AssertionError, e:
      self.verificationErrors.append(str(e))
    try:
      self.assertEqual(car.wheel_count, 4)  # Failure!
    except AssertionError, e:
      self.verificationErrors.append(str(e))


if __name__ == "__main__":
    unittest.main()
