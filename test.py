import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(True, True)

    def test_main(self):
        test_data = 'Test Name'
        res = main.hello(test_data)
        self.assertTrue(type(res) == str)

    def test_pythagorean(self):
        res = main.pythagorean(3, 4)

        self.assertTrue(type(res) == float)

        self.assertEqual(res, 5)

    def test_pythagorean_errors(self):
        with self.assertRaises(Exception):
            main.pythagorean(3, 0)

        with self.assertRaises(TypeError):
            main.pythagorean(3, '4')


if __name__ == '__main__':
    unittest.main()
