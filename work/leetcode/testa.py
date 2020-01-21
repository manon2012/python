def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n
r=bubble_sort([3,2,1,100,0,9,100,0])
print (r)

def select_sort(n):
    for i in range(len(n)-1):
        min_index=i
        for j in range(i,len(n)):
            if n[j]<n[min_index]:
                min_index =j
        n[i],n[min_index]=n[min_index],n[i]
    return n

r=select_sort([3,2,1,0,100,9])
print (r)

def insert_sort(n):
    for i in range(1,len(n)):
        j=i-1
        key=n[i]
        while j>=0 and n[j]>key:
            n[j+1]=n[j]
            j-=1
        n[j+1]=key

    return n
r=insert_sort([3,2,1,0,100,2])
print (r)

