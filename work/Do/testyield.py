
# def gen(n):
#     for i in n:
#         yield i
#
# g=gen([1,2,3])
# print (g.__dir__())
# print (g)
# for i in g:
#     print (i)

nested=[[1],[2,2],[3,3,3]]

# def flatten(nested):
#     for ele in nested:
#         for i in ele:
#             #print (i)
#             yield i
# #flatten(nested)
#
# for i in flatten(nested):
#     print (i)

def flatten(nested):

        try:
            for sublist in nested:
                for ele in flatten(sublist):
                    yield ele
        except TypeError:
            yield  nested
print (list(flatten([[1,[100]],[2,2],[3,3,3]])))
