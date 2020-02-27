import unittest
from FizzBuzz import FizzBuzz
import sys


class FizzBuzzTest(unittest.TestCase):

    def test_ExpectFizz_When_3_Is_Input(self):
        self.assertEqual(FizzBuzz(3), 'Fizz')

    def test_ExpectBuzz_When_5_Is_Input(self):
        self.assertEqual(FizzBuzz(5), 'Buzz')

    def test_ExpectFizzBuzz_When_15_Is_Input(self):
        self.assertEqual(FizzBuzz(15), 'FizzBuzz')


if __name__ == '__main__':
    for i in range(1, 100):
        print('{0} {1}'.format(i, FizzBuzz(i)))
    unittest.main()
