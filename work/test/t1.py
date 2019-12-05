import unittest
from p1128 import Runmain

class TestDemo(unittest.TestCase):

    def setup(self):
        self.r1 = Runmain()

    def tearDown(self):
        pass

    def test_01(self):
        print ("this is number 1")

    def test_02(self):
        print ("this is number 2")

    def test_03(self):

        url = 'http://***/account/login'
        data = {
            "username": "***01",
            "password": "password",
        }

        res=self.r1.

if __name__ == '__main__':

    suit=unittest.TestSuite()
    suit.addTests(TestDemo('test_01'))

    run=unittest.TextTestRunner()
    run(suit)