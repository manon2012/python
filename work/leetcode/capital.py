def capital(word):
    if word == word.title():
        return True
    else:
        return False

r=capital("ABC")
print (r)


mylist = ["a", "b", "a", "c", "c"]
mylist = dict.fromkeys(mylist)
print(mylist)

print ('Hello'=="Hello")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
import os
os.path.commonprefix()