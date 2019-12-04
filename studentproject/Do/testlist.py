a=[1,9,0,2]  # out [0,1,2,9]

# a.sort()
newa=[]
for i in range(len(a)):
    newa.append(min(a))
   # a.pop(a.index(min(a)))
    a.remove(min(a))
print (newa)


# print (a)

#a.reverse()
# print (a)
#
# b=list(reversed(a))
# print (b)

