import unittest
# Original functions, modified to return values instead of printing
def myfunc1(my_age: int, other_age: int) -> bool:
    return my_age == other_age

def myfunc2(birth_town: str, country: str) -> str:
    return f'I live in {birth_town} in {country}'

# Unit test using unittest library
class TestMyFuncs(unittest.TestCase):
    # Shared setup for all tests
    def setUp(self):
        self.shared_args = {
            'my_age': 42,
            'other_age': 10,
            'birth_town': 'Newcastle',
            'country': 'UK'
        }
    def test_myfunc1_equal_ages(self):
        self.assertTrue(myfunc1(self.shared_args['my_age'], self.shared_args['other_age']))

    def test_myfunc1_different_ages(self):
        self.assertFalse(myfunc1(self.shared_args['my_age'], self.shared_args['other_age']))

    def test_myfunc2(self):
        self.assertEqual(myfunc2(self.shared_args['birth_town'], self.shared_args['country']), 'I live in Newcastle in France')

if __name__ == '__main__':
    unittest.main()