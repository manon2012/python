

a={"a":1,"b":2,"c":3}
for i in enumerate(a.items(),1):
    print (i)

# print (a["sdfjlk"])
from collections import Counter

print (Counter(a))

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])

p=point(1,2)
print (p)