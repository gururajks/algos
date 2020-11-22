import os, json
import collections
from collections import defaultdict

proposal_map = defaultdict(dict)


def voter_rank(line):
    counts = line.split('|')
    for count in counts:

        proposal, option, votes = count.split(',')
        # print(proposal, option, votes)
        if proposal in proposal_map:
            votes_count = proposal_map[proposal]
            if option in votes_count:
                votes_count[option] += int(votes)
            else:
                votes_count[option] = int(votes)
        else:
            proposal_map[proposal] = {option: int(votes)}


def print_val():
    sorted_proposal_keys = sorted(proposal_map.items(), key=lambda x: x[0])

    for proposal, votes_dict in sorted_proposal_keys:

        sorted_votes = sorted(votes_dict.items(), key=lambda x: (-x[1], x[0]))
        count = 1

        for option_key, _ in sorted_votes:
            print("{},{},{}".format(proposal, count, option_key))
            count += 1


def main():
    s = (
        "Cafeteria Meals,Lunch only,211|Cafeteria Meals,Breakfast and lunch,58|On site child care,Yes,802|Cafeteria "
        "Meals,Lunch and dinner,58|Cafeteria Meals,Lunch only,127|On site child care,No,43")
    voter_rank(s)
    print_val()


if __name__ == "__main__":
    main()
