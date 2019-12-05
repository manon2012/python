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