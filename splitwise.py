import os, json
import collections
from collections import defaultdict
from functools import reduce
import heapq


class Splitwise:

    def __init__(self):
        self.balance = defaultdict(lambda: defaultdict(int))

    def paid(self, user1, user2, amt):
        self.balance[user1][user2] += amt
        self.balance[user2][user1] -= amt

    def get_balance(self, user):
        outstanding = self.balance[user]
        total_amt = 0
        for _, amt in outstanding.items():
            total_amt += amt

        return total_amt

    def settle_group(self, transactions):
        total_sum = reduce(lambda x, y: x + y[1], transactions, 0)
        each = round(total_sum / len(transactions), 1)
        print(each)
        outstandings = defaultdict(int)
        pos_group = []
        neg_group = []
        for name, amt in transactions:
            outstandings[name] += (amt - each)
            if amt - each > 0:
                heapq.heappush(pos_group, (amt - each, name))
            elif amt - each < 0:
                heapq.heappush(neg_group, (each - amt, name))


        print()
        edges = []
        while pos_group and neg_group:
            pos_amt, name1 = heapq.heappop(pos_group)
            neg_amt, name2 = heapq.heappop(neg_group)
            rem = pos_amt
            if pos_amt > neg_amt:
                rem = neg_amt
                heapq.heappush(pos_group, (pos_amt - neg_amt, name1))
            elif pos_amt < neg_amt:
                rem = pos_amt
                heapq.heappush(neg_group, (neg_amt - pos_amt, name2))
            edges.append(f"{name2} -> {name1} : {rem : .2f}")

            print(pos_group, neg_group)
        print(edges)



if __name__ == "__main__":
    s = Splitwise()
    # s.paid('Doofu', 'Deepu', 30)
    # s.paid('Doofu', 'Deepu', 60)
    # s.paid('Deepu', 'Doofu', 50)

    trans = [
        ['Deepu', 100],
        ['Doofu', 50],
        ['Dee', 100],
        ['Doo', 400],
        ['Pu', 600],
    ]

    s.settle_group(trans)
