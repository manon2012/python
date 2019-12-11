# import requests
#
# requests.get('https://api.github.com')

sta="abca"
#
a=[]
for i in sta:
    if i not in a:
        a.append(i)
        continue
    else:
        print (i)
        break
print (a)



a=["a","b","c","a"]
print ("a" in a)

print ("d" in a)
print ("a" not in a)

def test(a,b=[]):
    b.append(a)
    print (b)

test(1)
test(1)



#
# a=123
#
import copy
#
# b=copy.copy(a)
# c=copy.deepcopy(a)
#
# a=456

# a=[1,2,3,["a","b","c"]]
# b=copy.copy(a)
# c=copy.deepcopy(a)
#
# print (id(a),id(b),id(c))
# a[3][0]=100
# print (a,b,c)


stra="aaa"
for i in stra:
    if stra.count(i)==1:
        print (i)
        break







import sys
print(sys.modules)

import hashlib
print (hash("abc"))
print (hash("abc"))
print (hash("abc"))



# def f(n):
#     print (n)
#     n+=1
#     f(n)
# f(1)


import  os
print ([d for d in os.listdir('.')])


