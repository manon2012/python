a={"a":1,"c":3,"b":10,}

print (list(a.items()))
print (sorted(a))

aa=list(sorted(a.items()))
aa.sort(key=lambda x:x[1])
print (aa)


print (list(a.keys())[list(a.values()).index(10)])
print (a.values())



