import os, json
import collections


def add_one(arr):
    last_num = arr[-1] + 1
    arr[-1] = last_num % 10
    idx = len(arr) - 2
    borrow = last_num // 10

    while idx >= 0 and borrow > 0:
        num = arr[idx] + borrow
        arr[idx] = num % 10
        borrow = num // 10
        idx -= 1

    return arr


def main():
    print(add_one([1, 2, 9]))


if __name__ == "__main__":
    main()
