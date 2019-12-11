import json

a={"china":{"bj":"010","tj":"020"}}

print (a)
print (type(a))
#
# b=json.dumps(a)
# print (b)
# print (type(b))

with open("result","w") as fp:
    json.dump(a,fp)







