a={'name':'tom','age':21}
import copy

b=a.copy()
c=copy.deepcopy(a)

print (id(a),id(b),id(c))
a['name']='newtom'
print (a)
print (b)
print (c)


aa={'name':'tom','hobby':["girl","money"]}
bb=aa.copy()
cc=copy.deepcopy(aa)
print (id(aa),id(bb),id(cc))

aa['hobby'].append("stock")
print (aa)
print (bb)
print (cc)




