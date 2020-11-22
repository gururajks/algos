def merge(arr_input, low, high, mid):
    buffer = []
    count_left, count_right = low, mid
    while count_left < mid and count_right <= high:
        print(count_left)
        buffer.append(min(arr_input[count_right], arr_input[count_left]))
        if arr_input[count_left] <= arr_input[count_right]:
            count_left += 1
        else:
            count_right += 1

    while count_left < mid:
        buffer.append(arr_input[count_left])
        count_left += 1

    while count_right <= high:
        buffer.append(arr_input[count_right])
        count_right += 1

    i, j = low, 0
    while i <= high and j < len(buffer):
        arr_input[i] = buffer[j]
        i += 1
        j += 1
    print(buffer)


def merge_sort(arr_input):
    def divide_arr(arr, low, high):
        if low < high:
            mid = (low + high) // 2
            divide_arr(arr, low, mid)
            divide_arr(arr, mid + 1, high)
            merge(arr, low, high, mid)

    divide_arr(arr_input, 0, len(arr_input) - 1)


inp = [3, 23, 12, 0, 323, 333]
merge_sort(inp)
print(inp)
