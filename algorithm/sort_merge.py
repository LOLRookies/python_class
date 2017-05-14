def merge(list_a, list_b):
    index_a = 0
    index_b = 0
    list_c = []

    while index_a < len(list_a) and index_b < len(list_b):
        if list_a[index_a] < list_b[index_b]:
            list_c.append(list_a[index_a])
            index_a +=1
        else:
            list_c.append(list_b[index_b])
            index_b +=1
    return list_c



def mergeSort(array):
    # sort the array
    if len(array) <= 1:
        return array
    else:
        left = array[:len(array)/2]
        right = array[len(array)/2:]

        assorted_left = mergeSort(left)
        assorted_right = mergeSort(right)

        merged = merge(assorted_left, assorted_right)
        return merged



