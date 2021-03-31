import os, json
import collections


#
# // Teacher
# // S - 0.9 - S - 0.9 - S
# // | | |
# // 0.5
# 0.5
# // | | |
# // S - - S - 0.45 - S
# // | | |
# // 0.25
# // | | |
# // S - - S - 0.225 - S

# 0.9 * 0.9 = 0.81

# 1 - (1 - 0.9) * (1 - 0.5)
#
#
# h - 0.9
# v - 05


# 0, 0.
# 2, 0
# 1, 1

# [(0, 0), (1, 0), (1, 1)]
# h - 0.9
# v = 2 * v
def caught(h, v, path):
    if not path:
        return 0
    v *= 2
    # h - 0.9, v = 1
    curr_prob = 1
    idx = 0
    directions = {
        (0, -1): (1, 1),
        (0, 1): (1, 1),
        (1, 0): (1 / 2, 1 / 2),
        (-1, 0): (2, 2)

    }
    while idx + 1 < len(path):

        s1_row, s1_col = path[idx]
        s2_row, s2_col = path[idx + 1]

        nh, nv = directions[s2_row - s1_row, s2_col - s2_row]  # 1, 1
        # 1, 1
        h = nh * h  # 0.45
        v = nv * v  # 0.5
        if abs(s2_row - s1_row) > 0:
            curr_prob *= (1 - v)
        else:
            curr_prob *= (1 - h)

        idx += 1

    return 1 - curr_prob, h, v


def get_init_hv(init_pos, h, v):
    row, col = init_pos
    if row > 0:
        h = h // (2 ** (row - 1))
        v = v // (2 ** (row - 1))

    return h, v


def main():
    print(caught(0.9, 0.5, [(0, 0), (1, 0), (1, 1)]))


if __name__ == "__main__":
    main()
