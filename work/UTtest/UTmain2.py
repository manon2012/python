
import unittest
from UTtestcase import test01

class newmain(unittest.TestCase):
    def setup(self):
        pass
    def tearDown(self):
        pass
    def test_001(self):
        a=test01.newcal(1,2)
        self.assertEqual(a.newadd(),3)

print (newmain.mro())