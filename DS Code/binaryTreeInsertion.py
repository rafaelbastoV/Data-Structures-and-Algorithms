def binary_insert(arr, value):
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        currentValue = arr[middle]

        if currentValue < value:
            left = middle + 1
        elif currentValue > value:
            right = middle - 1
        else:
            arr.insert(middle, value)
            return arr

    arr.insert(left, value)
    return arr

print(binary_insert([1,5,8,10,20,22,30,31,32,43,49], 0))

