#
# a=[1,2,3]
# for i in a:
#     a[index(i)]=i+1


a=[1,2,3,2]
print (a.index(2))
# for i in a:
#     a[a.index(i)]+=1
# print (a)   #[4, 3, 3, 2]

for i in range(len(a)):
    a[i]+=1
print(a)

for i in range(len(a)):
    a.pop()

print (a)

a=[1,2,3,2]
b=a[:]
for i in b:
    a.remove(i)
print (a)

a={'a':1,'b':2,'c':3}
# del a['a']
# print (a)

b=a.keys()
print (list(b))
for i in list(b):
    del a[i]
print (a)
