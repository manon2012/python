def findRestaurant( list1, list2):
    for item in list1:
        if item in list2:
            return item
        
r=findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])
print (r)


