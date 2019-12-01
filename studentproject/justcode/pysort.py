
def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
    return n

print (bubble_sort([3,2,1,9,8,7,0]))


def new(n):
    i=0
    while i <len(n)-1:
        j=0
        while j<len(n)-1-i:
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
            j+=1
        i+=1
    return  n

print (new([3,2,1,9,8,7,0]))




def select_sort(n):
    for i in range(len(n)-1):
        min_index=i
        for j in range(i,len(n)):
            if n[j]<n[min_index]:
                min_index=j
        n[i],n[min_index]=n[min_index],n[i]
    return  n
print (select_sort([1,9,8,5,7,22,1]))



def new(n):
    i=0
    while i<len(n)-1:
        j=0
        min_index=i
        while i<j<len(len(n)):
            if n[j]<n[min_index]:
                min_index=j
            j+=1
        n[i], n[min_index] = n[min_index], n[i]
        i+=1
    return  n

print (new([3,2,1,7,8,9]))