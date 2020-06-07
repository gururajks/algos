import os, json
import collections


def quicksort(arr, start, end) -> int:
    pivot = start
    i = start
    while i < end:
        if arr[i] < arr[end]:
            arr[i], arr[pivot] = arr[pivot], arr[i]
            pivot += 1
        i += 1

    arr[pivot], arr[end] = arr[end], arr[pivot]
    return pivot


def divide(arr, start, end):
    if start < end:
        pivot = quicksort(arr, start, end)
        divide(arr, start, pivot - 1)
        divide(arr, pivot + 1, end)


if __name__ == "__main__":
    arr_input = [78, 3, 1, 0, -11, 14, 20]
    divide(arr_input, 0, len(arr_input) - 1)
    print(arr_input)
