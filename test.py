import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_trivial(self):
        self.assertEqual(True, False)

    def test_main(self):
        test_data = 'Test Name'
        res = main.hello(test_data)
        self.assertTrue(type(res) == str)


if __name__ == '__main__':
    unittest.main()
