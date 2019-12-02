import unittest

class cal():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
    def caladd(self):
        return self.a + self.b
    def caldiv(self):
        return (self.a)/(self.b)


class test_unit(unittest.TestCase):
    def setUp(self):
        print("before everyrun")

    def tearDown(self):
        print ("after everyrun")
    @classmethod
    def setUpClass(cls):
        print ("one class run once")
        #c1 = cal(10, 10) why not work?

    def test_01(self):
        c1=cal(10,10)
        self.assertEqual(c1.caladd(),20,"not equal")
    def test_02(self):
        c2 = cal(10, 1)
        self.assertEqual(c2.caldiv(),10)

if __name__ == '__main__':
    unittest.main()



