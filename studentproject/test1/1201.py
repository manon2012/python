import copy,os
a=[1,2,3,[11,22]]
b=copy.deepcopy(a)

print (a==b)
print (a is b)
print (id(a),id(b))
a[3][0]=22

print (a)
print (b)

#
# def func(n):
#     for i in n:
#         i+=1
#         print (i)
#     return  n

def func2(n):
    for i in range(len(n)):
        n[i]= n[i]+1
    return  n
#
# print (map(func2,[1,2,3]))
#
# print( func2([1,2,3]))
# print ([x+1 for x in [1,2,3]])
#
# map()


# def f(n):
#     return int(n)
#
# n=['1','2','3']
#
# print (map(f,n))


n=['1','2','3']
a=((map(lambda x:int(x),n)))
print (a.__dir__())
print (list(a))

n=[1,22,333]
print (list(filter(lambda x:len(str(x))==2,n)))


import unittest

class cal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def caladd(self):
        a=int(self.a)
        b=int(self.b)
        return self.a +self.b

class TestU(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("only once")
        d = cal(10, 10)
    def setup(self):
        print ('before everycase')
        #d=cal(10,10)

    def tearDown(self):
        print ("after everycase")
    def test_01(self):

        self.assertEqual(self.d.caladd(),20)

    def test_02(self):
        pass


if __name__ == '__main__':
    unittest.main()



