def findRestaurant( list1, list2):
    for item in list1:
        if item in list2:
            return item
        
r=findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
print (r)


# filter=["av","japan","xiaodao"]
# content=input("please input:")
# for i in filter:
#     if i in content:
#         content=content.replace(i,"***")
# print (content)
# c=content.split(" ")
# for i in c:
#     if i in filter:
#         c[c.index(i)]="***"
# print ("".join(c))

def sebsequence(a,b):
    sum=0
    j=0
    for i in range(len(b)-1):
        if b[i] == a[j]:
            sum += 1
            if j<len(a)-1:
                j+=1
            if j==len(a)-1:
                break

    return sum==len(a)

r=sebsequence("abc","aaabbbccc")
print (r)




