def binarySearch(array, value):
    print("array: ", array)
    print("value: ", value)
    array.sort()

    low = 0
    high = len(array) - 1

    print("low: ", low)
    print("high: ", high)

    while low <= high:
        mid = (low + high) // 2
        print("mid: ", mid)
        if array[mid] == value:
            print("output: ", [True, mid])
            return [True, mid]
        elif array[mid] < value:
            low = mid + 1
            print("low: ", low)
        else:
            high = mid - 1
            print("high: ", high)

    print("output: ", [False, None])
    return [False, None]
            
#print(binarySearch([1, 2, 3, 4, 5], 3))