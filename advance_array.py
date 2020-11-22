import os, json
from total_time import total_time


# O(n) and O(n)
@total_time
def advance_array(arr):
    dp = [False] * len(arr)
    dp[0] = True

    for idx, max_step in enumerate(arr):
        if dp[idx]:
            for i in range(idx, min(idx + max_step + 1, len(arr))):
                dp[i] = True

    return dp[-1]


def main():
    arr = [3, 2, 0, 0, 2, 0, 1]
    print(advance_array(arr))
    arr1 = [3, 3, 1, 0, 2, 0, 1]
    print(advance_array(arr1))
    pass


if __name__ == "__main__":
    main()
