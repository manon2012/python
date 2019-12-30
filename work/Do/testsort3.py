<<<<<<< HEAD

=======
>>>>>>> fa18662c7df3c24470bfae36b878e5cf1d7121a0
def bubble_sort(n):
    for i in range(len(n)-1):
        for j in range(len(n)-i-1):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
<<<<<<< HEAD
    return  n

print (bubble_sort([3,2,1,100]))
=======
    return n

print (bubble_sort([3,2,1]))
>>>>>>> fa18662c7df3c24470bfae36b878e5cf1d7121a0


def select_sort(n):
    for i in range(len(n)-1):
        min_index=i
<<<<<<< HEAD
        for j in range(i, len(n)):
            if n[j]<n[min_index]:
                min_index=j
        n[i],n[min_index]=n[min_index],n[i]
    return  n

print (select_sort([3,2,1,9,0]))


def insert_sort(n):
    for i in range(len(n)-1):
=======
        for j in range(i+1,len(n)):
            if n[j]<n[min_index]:
                min_index=j
        n[i],n[min_index]=n[min_index],n[i]
    return n

print (select_sort([3,2,1,100]))


def insert_sort(n):
    for i in range(1,len(n)):
>>>>>>> fa18662c7df3c24470bfae36b878e5cf1d7121a0
        key=n[i]
        j=i-1
        while j>=0 and n[j]>key:
            n[j+1]=n[j]
            j-=1
<<<<<<< HEAD
        n[j+1]=key
    return  n

print (insert_sort([3,2,1,0,100]))
=======
         n[j+1]=key
    return n

print(insert_sort([3,2,1]))


>>>>>>> fa18662c7df3c24470bfae36b878e5cf1d7121a0
