def countPrimes( n):
    """
    :type n: int
    :rtype: int
    """

    for i in range(2, n):

        if n % i == 0:
            # print ("not p")
            # return False
            break
    else:
        return True

# b = list(filter(countPrimes, range(2, 10)))
# print (b)
def getsum(n):
    # a=[]
    b = list(filter(countPrimes, range(2, n)))
    # print (b)
    # a.extend(b)
    print(len(b))
getsum(10)