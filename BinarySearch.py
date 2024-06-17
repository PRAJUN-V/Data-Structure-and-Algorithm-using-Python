def binary_search(array, element):
    min_index = 0
    max_index = len(array)
    while min_index <= max_index:
        middle_index = (min_index + max_index) // 2
        if array[middle_index] == element:
            return middle_index
        elif array[middle_index] < element:
            min_index = middle_index + 1
        elif array[middle_index] > element:
            max_index = middle_index - 1
    return -1

if __name__ == "__main__":
    # For binary search the array should be in sorted order.
    arr = [-67, -56, -1, 2, 3, 9, 19, 283, 789]
    for i in arr:
        print(binary_search(arr, i))
    print(binary_search(arr, 4))
