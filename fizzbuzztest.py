import unittest
from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_return_one_when_provided_with_one(self):
        self.assertEqual('1', fizzbuzz(1))

    def test_should_return_fizz_when_provided_with_three(self):
        self.assertEqual('fizz', fizzbuzz(3))

    def test_should_return_fizz_when_provided_with_five(self):
        self.assertEqual('buzz', fizzbuzz(5))

if __name__ == '__main__':
    unittest.main()