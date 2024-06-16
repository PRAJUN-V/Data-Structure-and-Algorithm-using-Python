def my_own_hash_function(data) -> int:
    if isinstance(data, bool):
        return 1 if data else 0

    if isinstance(data, int):
        return data

    elif isinstance(data, float):
        return int(data)

    elif isinstance(data, str):
        return len(data)

    elif isinstance(data, (list, set, tuple, dict)):
        return len(data)

    else:
        raise TypeError('Unsupported datatype')

if __name__ == '__main__':
    print(my_own_hash_function(True))      # Output: 1
    print(my_own_hash_function(False))     # Output: 0
    print(my_own_hash_function(123))       # Output: 123
    print(my_own_hash_function(12.34))     # Output: 12
    print(my_own_hash_function("hello"))   # Output: 5
    print(my_own_hash_function([1, 2, 3])) # Output: 3
    print(my_own_hash_function({1, 2, 3})) # Output: 3
    print(my_own_hash_function((1, 2, 3))) # Output: 3
    print(my_own_hash_function({"a": 1, "b": 2})) # Output: 2
