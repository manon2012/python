
str1= "a,b,c"

for i in str1:
  print i



import sys
lst = __file__.split('/')
base_path  = '/'.join(lst[:-2])
sys.path.append(base_path)   # python解释器相关
from core import main

if __name__ == '__main__':
    main.entry()

rom core import auth


def entry():
    print ("welcome to 3T system")
    auth.login()



if __name__ == '__main__':
    entry()
