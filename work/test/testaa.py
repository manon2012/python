import unittest

class MyTest(unittest.TestCase):
    def setup(self):
        print ("it is baseline")

    def test_01(self):
        self.assertEqual('a','a')

    def test_02(self):
        self.assertIn('a','abc')


    def tearDown(self):
        print ("it is clear")


if __name__ == '__main__':
    unittest.main()