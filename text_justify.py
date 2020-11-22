import os, json
import collections

'''
We are building a word processor and we would like to implement a "reflow" functionality that also applies full justification to the text.

Given an array containing lines of text and a new maximum width, re-flow the text to fit the new width. Each line should have the exact specified width. If any line is too short, insert '-' (as stand-ins for spaces) between words as equally as possible until it fits.

Note: we are using '-' instead of spaces between words to make testing and visual verification of the results easier.

lines = [ "The day began as still as the",
          "night abruptly lighted with",
          "brilliant flame" ]

reflowAndJustify(lines, 24) ... "reflow lines and justify to length 24" =>

        [ "The--day--began-as-still",
          "as--the--night--abruptly",
          "lighted--with--brilliant",
          "flame" ] // <--- a single word on a line is not padded with spaces

reflowAndJustify(lines, 25) ... "reflow lines and justify to length 25" =>

        [ "The-day-began-as-still-as"
          "the-----night----abruptly"
          "lighted---with--brilliant"
          "flame" ]

reflowAndJustify(lines, 26) ... "reflow lines and justify to length 26" =>

        [ "The--day-began-as-still-as",
          "the-night-abruptly-lighted",
          "with----brilliant----flame" ]

reflowAndJustify(lines, 40) ... "reflow lines and justify to length 40" =>

        [ "The--day--began--as--still--as-the-night",
          "abruptly--lighted--with--brilliant-flame" ]

reflowAndJustify(lines, 14) ... "reflow lines and justify to length 14" =>

        ['The--day-began',
         'as---still--as',
         'the------night',
         'abruptly', 
         'lighted---with', 
         'brilliant', 
         'flame']
'''


# 6 dashes - 5 words
# 6 // 4 = 1 (len(words) - 1)
# 6 % 4 = 2
# 2 extra beginning
# 4 dashes , 3 words
# 4 // 2 = 2


def insert_text(curr_list, curr_len, max_length):
    equal_dashes = no_of_dashes = max_length - curr_len
    remaining_dashes = 0
    if len(curr_list) - 1 > 1:
        equal_dashes = no_of_dashes // (len(curr_list) - 1)
        remaining_dashes = no_of_dashes % (len(curr_list) - 1)

    justified = ""

    for idx in range(len(curr_list) - 1):
        word = curr_list[idx]
        justified += word + '-' * equal_dashes + '-' * (1 if remaining_dashes > 0 else 0)
        remaining_dashes -= 1

    justified += curr_list[-1]

    return justified


def wrapLines(arr, max_length):
    output = []
    curr_list = []
    curr_len = 0
    for sentence in arr:
        # subtracting the possible dashes
        words = sentence.split(' ')
        for word in words:
            if curr_len + len(word) >= max_length - (len(curr_list) - 1):
                output.append(insert_text(curr_list, curr_len, max_length))
                curr_list = []
                curr_len = 0

            curr_len += len(word)
            curr_list.append(word)

    if curr_list:
        output.append(insert_text(curr_list, curr_len, max_length))
    
    return output


lines = ["The day began as still as the", "night abruptly lighted with", "brilliant flame"]
test_reflow_width1 = 24
print(wrapLines(lines, test_reflow_width1))
test_reflow_width2 = 25
print(wrapLines(lines, test_reflow_width2))
test_reflow_width3 = 26
print(wrapLines(lines, test_reflow_width3))
test_reflow_width4 = 40
print(wrapLines(lines, test_reflow_width4))
test_reflow_width5 = 14
print(wrapLines(lines, test_reflow_width5))



# Time: O(n) and space O(n)


def main():
    pass


if __name__ == "__main__":
    main()
