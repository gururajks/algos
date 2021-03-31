import os, json
import collections

from itertools import zip_longest
from typing import List, Tuple

"""
Problem description:
    It is very typical for us to compare a reference transcript with an ASR
    output hypothesis transcript. Usually, we align the words in the reference
    and the hypothesis, and use that to calculate the word error rate. However,
    it would be nice to also align the reference and hypothesis at a sentence
    level, so we could calculate more metrics in the future.
    The goal of this problem is to create the sentence alignment, given the
    punctuation in the reference transcript, and the word alignment between the
    reference and the hypothesis.
"""

"""
Test 0:
    ref: I like food. Food tastes good!
    hyp: i like food food tastes bad
"""
test0_punc = ['', '', '.', '', '', '!']
test0_alignment = [
    ("i", "i"),
    ("like", "like"),
    ("food", "food"),
    ("food", "food"),
    ("tastes", "tastes"),
    ("good", "bad"),
]

test0_expected = [
    ("i like food.", "i like food."),
    ("food tastes good!", "food tastes bad!")
]

"""
Test 1:
    ref: I like food. Food tastes good!
    hyp: i dont like food food bad
"""
test1_punc = ['', '', '.', '', '', '!']
test1_alignment = [
    ("i", "i"),
    ("<ins>", "dont"),
    ("like", "like"),
    ("food", "food"),
    ("food", "food"),
    ("tastes", "<del>"),
    ("good", "bad"),
]

test1_expected = [
    ("i like food.", "i dont like food."),
    ("food tastes good!", "food bad!")
]

"""
Test 2:
    ref: I like food. Food tastes good! So does cake.
    hyp: i dont like food good so does cake soda
"""
test2_punc = ['', '', '.', '', '', '!', '', '', '.']
test2_alignment = [
    ("i", "i"),
    ("<ins>", "dont"),
    ("like", "like"),
    ("food", "food"),
    ("food", "<del>"),
    ("tastes", "<del>"),
    ("good", "good"),
    ("so", "so"),
    ("does", "does"),
    ("cake", "cake"),
    ("<ins>", "soda"),
]

test2_expected = [
    ("i like food.", "i dont like food."),
    ("food tastes good!", "good!"),
    ("so does cake.", "so does cake soda."),
]

"""
Test 3:
    ref: I like food. Food tastes good! So does cake.
    hyp: i like tastes good my friend so does cake
    Note that for this test, <ins> next to punctuation can be dealt with either
    by including the insertions in the previous or next sentence, the choice is
    arbitrary. For this interview, we will put them in the next sentence.
"""
test3_punc = ['', '', '.', '', '', '!', '', '', '.']
test3_alignment = [
    ("i", "i"),
    ("like", "like"),
    ("food", "<del>"),
    ("food", "<del>"),
    ("tastes", "tastes"),
    ("good", "good"),
    ("<ins>", "my"),
    ("<ins>", "friend"),
    ("so", "so"),
    ("does", "does"),
    ("cake", "cake"),
]

test3_expected = [
    ("i like food.", "i like."),
    ("food tastes good!", "tastes good my friend!"),
    ("so does cake.", "so does cake."),
]


def check_tests(func):
    print("Running tests")
    res0 = func(test0_punc, test0_alignment)
    res1 = func(test1_punc, test1_alignment)
    res2 = func(test2_punc, test2_alignment)
    res3 = func(test3_punc, test3_alignment)
    try:
        assert res0 == test0_expected
        print("Test 0 OK!")
    except AssertionError:
        print("Test 0 Failed! Differences were:")
        for t0, t1 in zip_longest(test0_expected, res0):
            if t0 != t1:
                print(f"expected: {t0}")
                print(f"got: {t1}")
    try:
        assert res1 == test1_expected
        print("Test 1 OK!")
    except AssertionError:
        print("Test 1 Failed! Differences were:")
        for t0, t1 in zip_longest(test1_expected, res1):
            if t0 != t1:
                print(f"expected: {t0}")
                print(f"got: {t1}")
    try:
        assert res2 == test2_expected
        print("Test 2 OK!")
    except AssertionError:
        print("Test 2 Failed! Differences were:")
        for t0, t1 in zip_longest(test2_expected, res2):
            if t0 != t1:
                print(f"expected: {t0}")
                print(f"got: {t1}")
    try:
        assert res3 == test3_expected
        print("Test 3 OK!")
    except AssertionError:
        print("Test 3 Failed! Differences were:")
        for t0, t1 in zip_longest(test3_expected, res3):
            if t0 != t1:
                print(f"expected: {t0}")
                print(f"got: {t1}")


def create_sentence_alignments(ref_punc_list: List[str], word_alignment:
List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    """ Given a list of punctuation in the reference, and the
    (reference, hypothesis) word alignment, returns the (reference, hypothesis)
    sentence alignment.
    Args:
    :param ref_punc_list: A list of punctuation symbols, representing the
        optional punctuation for every word in the reference transcript
    :param word_alignment: An aligned list of pairs of words, where the first 
        element in the pair is from the reference, and the second from the
        hypothesis. The reference could be '<ins>', and the hypothesis could be 
        <del>, representing an insertion or deletion respectively.
    :returns: A list of (ref, hyp) sentence alignments
    """

    punc_idx = 0
    output = []
    idx = 0
    left_sentence, right_sentence = "", ""
    while idx < len(word_alignment):

        left, right = word_alignment[idx]
        if left == '<ins>':
            right_sentence += right + ' '
        elif right == '<del>':
            left_sentence += left + ' '
            punc_idx += 1
        else:
            existing_punc = ref_punc_list[punc_idx]
            left_sentence += left + ' '
            right_sentence += right + ' '
            if existing_punc == '.' or existing_punc == '!':
                if idx + 1 < len(word_alignment) and word_alignment[idx + 1][0] != '<ins>':

                    output.append((left_sentence[:-1] + existing_punc, right_sentence[:-1] + existing_punc))
                    left_sentence, right_sentence = "", ""
                else:
                    punc_idx -= 1

            punc_idx += 1

        idx += 1

    if left_sentence and right_sentence:
        punc = ""
        if punc_idx < len(ref_punc_list):
            punc = ref_punc_list[punc_idx]
        output.append((left_sentence[:-1] + punc, right_sentence[:-1] + punc))

    return output


if __name__ == "__main__":
    check_tests(create_sentence_alignments)

if __name__ == "__main__":
    main()