
data = [1,5,10,20,300,1000,20000]


def binary_search(target):
    # return target index
    # if not found return None
    left = 0
    right = len(data)
    while left < right:
        mid = (left + right) / 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            right = mid
        else:
            left = mid + 1

    return None


print binary_search(20000) # expect index 5


