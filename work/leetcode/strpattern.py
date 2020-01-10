def repeatedSubstringPattern(self, s: str) -> bool:
    substrings=[]
    #find possible substings, substring should start with first letter and end with the last letter.
    for i in range(len(s)-1):
        if s[i] == s[-1]:
            subs = s[:i+1]
            #check the length division, make run time faster
            if len(s) % len(subs) == 0:
                substrings.append(s[:i+1])
    for subs in substrings:
        if s.replace(subs,"") =="":
            return True
    return False

def r2(str):
    ss = (str * 2)[1:-1]
    print (ss)
    return str in ss
r=r2("abab")
print (r)

a="abababab"