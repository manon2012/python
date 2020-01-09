def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 1:
        return True
    for i in range(num):
        if i * i == num:
            return True
    return False


r1=isPerfectSquare(16)
r2=isPerfectSquare(1)
r3=isPerfectSquare(15)
print (r1)
print (r2)
print (r3)