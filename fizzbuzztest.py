import unittest
from fizzbuzz import fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    def test_should_return_one_when_provided_with_one(self):
        self.assertEqual('1', fizzbuzz(1))

if __name__ == '__main__':
    unittest.main()