

import unittest

class TestCount:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def doadd(self):
        return  self.a + self.b

class TestUt(unittest.TestCase):
    def setUp(self):
        print ("before...")

    def testdoadd(self):
        i=TestCount(1,2)
        print (i)
        self.assertEqual(i.doadd(),3,"not equal")
    def teststr(self):
        self.assertTrue(0)

    def tearDown(self):
        print ("after...")

if __name__ == '__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(TestUt("testdoadd"))
    print (suite)


    runner=unittest.TextTestRunner
    runner.run(suite)