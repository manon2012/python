
# def power2(n):
#     if n&(n-1)==0:
#         return True
#     else:
#         return False
#
# print (power2(8))
# print (power2(10))

def p3(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n /= 3

    return n == 1

print (p3(12))