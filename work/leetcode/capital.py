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