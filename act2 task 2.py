def binary_search(arr, target):
    # Magset ng starting and ending indexes
    low, high = 0, len(arr) - 1

    # Continue searching while there is a valid range
    while low <= high:
        # Hanapin ang middle index
        mid = (low + high) // 2

        # Check if the middle value is the target
        if arr[mid] == target:
            return mid

        # kung ang target ay mas mataas, search the right half
        elif arr[mid] < target:
            low = mid + 1

        # Otherwise, search the left half
        else:
            high = mid - 1

    # Return -1 kung hindi nmahanap ang target
    return -1


# Sorted list for binary search
numbers = [10, 20, 30, 40, 50, 60]

# Hanapin ang value 50 and print its index
print(binary_search(numbers, 50))