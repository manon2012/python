def anagram(a,b):
    aa="".join(sorted(a))
    bb="".join(sorted(b))
    if aa==bb:
        return True
    else: return False

r=anagram("abc","cbaa")
print (r)

