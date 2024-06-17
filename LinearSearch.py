def linear_search(array, element) -> int:
    """
    Perform a linear search for the element in the array.

    Parameters:
    array (list): The list to search within.
    element: The element to search for.

    Returns:
    int: The index of the element if found, otherwise -1.
    """
    index = 0
    for i in array:
        if i == element:
            return index
        index += 1
    return -1

if __name__ == "__main__":
    arr = [4, -4, 90, 7.8, 'b', ['hello']]
    print(linear_search(arr, 90))
    print(linear_search(arr, ["hello"]))
    print(linear_search(arr, 7))
    print(linear_search.__doc__)
