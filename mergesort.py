def merge_sort(arr, start, end):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    temp = [0] * (end - start + 1)

    temp_i, i, j = 0, start, mid + 1

    while i <= mid and j <= end:
        if (arr[i] < arr[j]):
            temp[temp_i] = arr[i]
            i += 1
        else:
            temp[temp_i] = arr[j]
            j += 1
        temp_i += 1

    while i <= mid:
        temp[temp_i] = arr[i]
        i += 1
        temp_i += 1

    while j <= end:
        temp[temp_i] = arr[j]
        j += 1
        temp_i += 1

    i = start
    while i <= end:
        arr[i] = temp[i - start]
        i += 1


input = [3, 6, 23, 12, 11]
merge_sort(input, 0, len(input) - 1)
print(input)