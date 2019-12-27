node={
   "node1":{"tpye":"linux","auth":{"name":"admin","passwd":123}},
    "node2":{"tpye":"esxi","auth":{"name":"root","passwd":123}},
}

print (node)
print (type(node))

import json
a=json.dumps(node)
print (a)
print (type(a))

b=json.loads(a)
print (b)
print (type(b))


#a=input("input:")

try:
    int(a)
except ValueError:
    print ("can't be 0")
except Exception as e:
    print (e)

nest=[1,2,3,4,5]
# for i in nest:
#     yield i
# print(i.next())

# def showit(n):
#     for i in n:
#         yield i
# g=showit(nest)
# for i in g:
#     print (i)
#
# print (type(g))
# print (dir(g))

a=nest.__iter__()
print (type(a))

while 1:
    try:
        print (a.__next__())
        print ("got it")
    except StopIteration as e:
        print (e)
        break
else:
    "test"



