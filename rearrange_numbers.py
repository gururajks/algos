import os, json
import collections


def rearrange_numbers(arr):
    arr.sort()
    for idx in range(1, len(arr) - 1, 2):
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

    return arr


def main():
    arr = [1, 5, 3, 56, 31, 5, 7, 8, 61, 81, 18]
    print(rearrange_numbers(arr))


if __name__ == "__main__":
    main()
