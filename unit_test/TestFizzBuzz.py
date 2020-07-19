import unittest
import fizzbuzz as fb

class TestFizzBuzz(unittest.TestCase):
    
    def test_multiple_of_three(self):
        self.assertEqual(fb.answer(6), 'Fizz')

    def test_multiple_of_five(self):
        self.assertEqual(fb.answer(20), 'Buzz')

    def test_multiple_of_three_and_five(self):
        self.assertEqual(fb.answer(15), 'FizzBuzz')

    def test_regular_numbers(self):
        self.assertEqual(fb.answer(2), 2)
        self.assertEqual(fb.answer(98), 98)

if __name__ == "__main__":
    unittest.main()

# >> python -m unittest TestFizzBuzz.py



