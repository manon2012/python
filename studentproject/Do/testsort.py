def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1-i):
            if n[j]>n[j+1]:
                n[j],n[j+1]= n[j+1],n[j]
    return  n

print (bubble_sort([3,2,1]))


def select_sort(n):
    for i in range(len(n)-1):
        min_index=i
        for j in range(i,len(n)):
            if n[j]<n[min_index]:
                min_index=j
        n[i],n[min_index]=n[min_index],n[i]
    return  n

print (select_sort([1,2,3,100,9,8]))


def insert_sort(n):   # 3 2 1
    for i in range(1,len(n)):
        key=n[i]
        j=i-1
        while j>=0 and n[j]>key:
            n[j+1]=n[j]
            j-=1
        n[j+1]=key
    return  n

print (insert_sort([3,2,1]))