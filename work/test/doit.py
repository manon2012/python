import json
result = json.loads(s) # s 就是你的字符串
for i in result:
    pirnt("Id:%(Id)s RepoTags:%(RepoTags)s" % i)


 list.sort() 方法只是为列表定义的，而 sorted() 函数可以接受任何可迭代对象。