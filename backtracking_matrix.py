"""

The conflict with your students escalates, and now they are hiding multiple words in a single word grid. Return the location of each word as a list of coordinates. Letters cannot be reused across words.

grid1 = [
    ['c', 'r', 'c', 'a', 'r', 's'],
    ['a', 'b', 'i', 't', 'n', 'b'],
    ['t', 'e', 'n', 'n', 't', 'i'],
    ['x', 's', 'i', 'i', 'p', 't']
]

words1_1 = [ "bit", "catnip", "cat" ]
words1_2 = [ "cat", "ten" ]

find_word_locations(grid1, words1_1)->
  [ [ (1, 5), (2, 5), (3, 5) ],
    [ (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (3, 4) ],
    [ (0, 0), (1, 0), (2, 0) ],
  ]
find_word_locations(grid1, words1_2)->
  [ [ (0, 2), (0, 3), (1, 3) ],
    [ (2, 0), (2, 1), (2, 2) ],
  ]

# Additional example

grid2 = [
	['b', 'a', 't'],
	['y', 'x', 'b'],
	['x', 'x', 'y'],
]

words2 = ["by", "bat"]

find_word_locations(grid2, words2)->
  [ [ (1, 2), (2, 2) ],
    [ (0, 0), (0, 1), (0, 2) ],
  ]

r = number of rows
c = number of columns
w = length of the word

"""




def dfs(grid, row, col, word, seen, st):
    if not word:
        return True, st

    for n_row, n_col in ((row + 1, col), (row, col + 1)):

        if 0 <= n_row < len(grid) and 0 <= n_col < len(grid[0]) and (n_row, n_col) not in seen:
            if grid[n_row][n_col] == word[0]:
                st.append((n_row, n_col))
                seen.add((n_row, n_col))
                found, st =  dfs(grid, n_row, n_col, word[1:], seen, st)
                if found:
                    return True, st
                st.pop()
                seen.remove((n_row, n_col))

    return False, st




def find_word_location(grid, words):

    seen = set()
    path = []

    path = find_indv_word_location(grid, words, 0, seen, path)

    return path


def find_indv_word_location(grid, words, idx, seen, path):

    if idx >= len(words):
        return True, path

    st = []
    word = words[idx]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0] and (i, j) not in seen:

                st.append((i, j))
                seen.add((i, j))
                found, st = dfs(grid, i, j, word[1:], seen, st)
                if found:
                    path.append(st)
#                     print(word, path)
                    word_found, path = find_indv_word_location(grid, words, idx + 1, seen, path)
                    if word_found:
                        return path
                st.pop()
                seen.remove((i, j))

    return False, path








# c - 1
# a - 1
# t - 1

# t - 2
# c - 1
# a - 1
from collections import Counter


def word_exist(string1, words):

    if not words or not string1:
        return None

    c_string = Counter(string1)


    for word in words:
        c_word = Counter(word)

        word_found = True
        for k, v in c_word.items():
            if c_string.get(k, 0) < v:
                word_found = False
                break
        if word_found:
            return word

    return None












# TODO --- Write your function


# TODO --- Call your function with the test cases from above

grid1 = [
    ['c', 'r', 'c', 'a', 'r', 's'],
    ['a', 'b', 'i', 't', 'n', 'b'],
    ['t', 'e', 'n', 'n', 't', 'i'],
    ['x', 's', 'i', 'i', 'p', 't']
]

words1_1 = ["bit", "catnip", "cat"]

print("answer", find_word_location(grid1, words1_1))
words1_2 = [ "cat", "ten" ]

grid2 = [
    ['b', 'a', 't'],
    ['y', 'x', 'b'],
    ['x', 'x', 'y'],
]
words2 = ["by", "bat"]


