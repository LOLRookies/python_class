#range
for x in range(3):
    print x

a = [5, 4, 1, 2, 3]

a.sort()
print a

b = [2, 8, 7, 5, 1]
print sorted(b)


# selection sort
def swap(A,x,y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp


def selectionsort( aList ):
    for i in range( len( aList ) ):
       # i = 1
        least = i # least means the position of minumum number
        for k in range( i + 1 , len( aList ) ):
            # k = 4
            if aList[k] < aList[least]:
                #least = 3
                least = k
        swap( aList, least, i )


