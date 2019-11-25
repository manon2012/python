import unittest

class Count():
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    def add(self):
        return  self.a + self.b

class TestAdd(unittest.TestCase):
    def setUp(self):
        print ("begin...")


    def test_01(self):
        i=Count(1,2)
        #print ("test_01 run")
        self.assertEqual(i.add(),3,"wrong")

    def test_02(self):
        self.assertIn("ca","ca","not in ")

    def tearDown(self):
        print ("end...")

if __name__ == '__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(TestAdd('test_01'))
    #suite.addTest(TestAdd('test_02'))

    runner=unittest.TextTestRunner
    runner.run(suite)