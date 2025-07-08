def merge_sorting_recursive(arr):
    if len(arr) > 1:
        left_arr = arr[: len(arr) // 2]
        right_arr = arr[len(arr) // 2 :]

        merge_sorting_recursive(left_arr)
        merge_sorting_recursive(right_arr)

        i = j = k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


list_1 = [2, 1, 5, 9, 6, 4, 3, 8, 7]
merge_sorting_recursive(list_1)

print(list_1)


def merge(arr, left, mid, right):
    """Merge two sorted subarrays: arr[left:mid+1] and arr[mid+1:right+1]"""
    left_part = arr[left : mid + 1]
    right_part = arr[mid + 1 : right + 1]

    i = j = 0  # Pointers for left and right parts
    k = left  # Pointer for main array

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort_iterative(arr):
    """Iterative Merge Sort"""
    n = len(arr)
    size = 1  # Start with subarrays of size 1

    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            merge(arr, left, mid, right)
        size *= 2  # Double the subarray size


# Example usage
arr = [5, 3, 8, 6, 2, 7, 4, 1]
merge_sort_iterative(arr)
print(arr)
