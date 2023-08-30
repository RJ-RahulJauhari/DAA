def partition(arr, left, right):
    p = arr[right]
    i = left
    j = right - 1

    while i < j:
        while arr[i] < p and i < right:
            i += 1
        while arr[j] > p and j > left:
            j += 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > p:
        arr[i], arr[right] = arr[right], arr[i]

    return i


def quicksort(arr, left, right):
    if left < right:
        partition_index = partition(arr, left, right)
        quicksort(arr, left, partition_index - 1)
        quicksort(arr, partition_index + 1, right)
    return arr