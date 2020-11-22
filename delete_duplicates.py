import os, json
import collections
from total_time import total_time

@total_time
def delete_duplicates(arr):
    pivot = 1
    for i in range(1, len(arr)):
        if arr[i - 1] != arr[i]:
            arr[pivot] = arr[i]
            pivot += 1

    for i in range(pivot, len(arr)):
        arr[i] = 0

    return arr


def main():
    arr = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    print(delete_duplicates(arr))


if __name__ == "__main__":
    main()
