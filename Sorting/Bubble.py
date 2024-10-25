def bubble_sort(nums):
    n = len(nums)

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        if not swapped:
            break  

nums = [5, 3, 8, 6, 7, 2]
bubble_sort(nums)
print(nums)
