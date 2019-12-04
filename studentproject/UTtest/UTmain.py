import unittest
from UTtestcase import test_01
class UTtest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        a1 = test_01.Cal(1, 2)
        self.assertEqual(a1.caladd(),3,"not equal")

    @unittest.skip
    def test_2(self):
        a2=test_01.Cal(0,1)
        self.assertEqual(a2.caladd(),1)

if __name__ == '__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(UTtest('test_1'))

    suite.addTest(UTtest('test_1'))

    run=unittest.TextTestRunner()
    run.run(suite)

