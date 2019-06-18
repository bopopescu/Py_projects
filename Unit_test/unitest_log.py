import unittest

# class TestCaseDemo2(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         print("*"*25)
#         print("QA Test Starts")
#         print("*" * 25)
#         print("\n\n")
#
#     def setUp(self):
#         print("QA test setup is done")
#
#     def test_methodA(self):
#         print("Runing method A")
#
#     def test_methonB(self):
#         print("Running method B")
#
#     def tearDown(self):
#         print("Test is done\n")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print("\n\n")
#         print("*" * 25)
#         print("End of QA unit testing")
#         print("*"*25)

class TestCaseDemo2(unittest.TestCase):

    def test_assertTrueFalse(self):
        a = True
        b = False
        self.assertTrue(a, "a is not True")
        self.assertFalse(b, "b is not false")

    def test_assertEqual(self):
        a, b = "Test", "Telst"
        self.assertEqual(a, b, msg="a is not equal to b")
if __name__ == "__main__":
    unittest.main(verbosity=2)