import unittest
import function


class FuncUnitTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(function.fib(10), 55)
        self.assertEqual(function.fib(20), 6765)
    def test_two(self):
        self.assertEqual(function.fib(5), 5)
        self.assertEqual(function.fib(15), 610)






if __name__=='__main__':
    unittest.main()