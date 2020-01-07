def callcalc(a):
    def calc(b):
        return  a*b
    return calc

a=callcalc(100)(100)
print (a)