from collections import defaultdict
from pprint import pprint

data = defaultdict(list)
data["2016-baby-center-girls"] = ["Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Riley", "Aria", "Zoe",
                                  "Charlotte", "Lily", "Layla", "Amelia", "Emily", "Madelyn", "Aubrey", "Adalyn",
                                  "Madison", "Chloe", "Harper", "Abigail", "Aaliyah", "Avery", "Evelyn", "Kaylee",
                                  "Ella", "Ellie", "Scarlett", "Arianna", "Hailey", "Nora", "Addison", "Brooklyn",
                                  "Hannah", "Mila", "Leah", "Elizabeth", "Sarah", "Eliana", "Mackenzie", "Peyton",
                                  "Maria", "Grace", "Adeline", "Elena", "Anna", "Victoria", "Camilla", "Lillian",
                                  "Natalie"]

data["2016-baby-center-boys"] = ["Jackson", "Aiden", "Lucas", "Liam", "Noah", "Ethan", "Mason", "Caden", "Oliver",
                                 "Elijah", "Grayson", "Jacob", "Michael", "Benjamin", "Carter", "James", "Jayden",
                                 "Logan", "Alexander", "Caleb", "Ryan", "Luke", "Daniel", "Jack", "William", "Owen",
                                 "Gabriel", "Matthew", "Connor", "Jayce", "Isaac", "Sebastian", "Henry", "Muhammad",
                                 "Cameron", "Wyatt", "Dylan", "Nathan", "Nicholas", "Julian", "Eli", "Levi", "Isaiah",
                                 "Landon", "David", "Christian", "Andrew", "Brayden", "John", "Lincoln"]

data["2015-baby-center-girls"] = ["Sophia", "Emma", "Olivia", "Ava", "Mia", "Isabella", "Zoe", "Lily", "Emily",
                                  "Madison", "Amelia", "Riley", "Madelyn", "Charlotte", "Chloe", "Aubrey", "Aria",
                                  "Layla", "Avery", "Abigail", "Harper", "Kaylee", "Aaliyah", "Evelyn", "Adalyn",
                                  "Ella", "Arianna", "Hailey", "Ellie", "Nora", "Hannah", "Addison", "Mackenzie",
                                  "Brooklyn", "Scarlett", "Anna", "Mila", "Audrey", "Isabelle", "Elizabeth", "Leah",
                                  "Sarah", "Lillian", "Grace", "Natalie", "Kylie", "Lucy", "Makayla", "Maya", "Kaitlyn"]

data["2015-baby-center-boys"] = ["Jackson", "Aiden", "Liam", "Lucas", "Noah", "Mason", "Ethan", "Caden", "Logan",
                                 "Jacob", "Jayden", "Oliver", "Elijah", "Alexander", "Michael", "Carter", "James",
                                 "Caleb", "Benjamin", "Jack", "Luke", "Grayson", "William", "Ryan", "Connor", "Daniel",
                                 "Gabriel", "Owen", "Henry", "Matthew", "Isaac", "Wyatt", "Jayce", "Cameron", "Landon",
                                 "Nicholas", "Dylan", "Nathan", "Muhammad", "Sebastian", "Eli", "David", "Brayden",
                                 "Andrew", "Joshua", "Samuel", "Hunter", "Anthony", "Julian", "Dominic"]

data["2015-us-official-girls"] = ["Emma", "Olivia", "Sophia", "Ava", "Isabella", "Mia", "Abigail", "Emily", "Charlotte",
                                  "Harper"]

data["2015-us-official-boys"] = ["Noah", "Liam", "Mason", "Jacob", "William", "Ethan", "James", "Alexander", "Michael",
                                 "Benjamin"]


# Write a function that given a name, returns an ascending rank sorted list of names of all lists where the given name appears.
# For example, given "sophia", function returns:
#  [
#    {list: "2016-baby-center-girls", rank: 1},
#    {list: "2015-baby-center-girls", rank: 1},
#    {list: "2015-us-official-girls", rank: 3}
#  ]

# dictionary dictionary -> name to idx(rank)
# O(1)

# aton

# an
# {
#   anna: [
#     { list: '2015-baby-center-girls', rank: 36 },
#     { list: '2016-baby-center-girls', rank: 46 }
#   ],
#   andrew: [
#     { list: '2015-baby-center-boys', rank: 44 },
#     { list: '2016-baby-center-boys', rank: 47 }
#   ],
#   anthony: [
#     { list: '2015-baby-center-boys', rank: 48 }
#   ]
# }


# name -> [(rank, key)]

def build_cache(data):
    cache = defaultdict(list)
    for k, names in data.items():
        for idx, name in enumerate(names):
            cache[name].append([k, idx + 1])

    return cache


def get_rank(cache, input_name):
    pprint(cache)
    output = []
    if input_name in cache:
        output = cache[input_name]
        output.sort(key=lambda x: x[1])

    return output


# pprint(get_rank(cache, "Sophia"))

class TrieNode:
    def __init__(self):
        self.names = []
        self.children = {}


class Trie:

    def __init__(self):
        self.node = {}

    def insert_node(self, name):
        root = self.node
        for letter in name:
            if letter not in root:
                root[letter] = {}
            root = root[letter]

        root['*'] = True

    def traverse(self, root, built_name, pre, names):
        if '*' in root:
            names.append(built_name)

        for k, children in root.items():
            if children == True:
                continue
            self._get_names(root[k], built_name + k, names)

            root.names.add(names)

    def build_cache(self):
        self.traverse(self.node, "", "", [])

    def _get_names(self, root, built_name, names):
        if '*' in root:
            names.append(built_name)

        for k, children in root.items():
            if children == True:
                continue
            self._get_names(root[k], built_name + k, names)

    def find_names(self, pre):
        root = self.node
        names = []
        for letter in pre:
            if letter in root:
                root = root[letter]

        self._get_names(root, pre, names)

        return names


def build_trie(names):
    t = Trie()
    for name in names:
        t.insert_node(name)

    return t


def autocomplete(t, cache, pre):
    names = t.find_names(pre)
    output = []
    for name in names:
        output.append([name, cache[name]])

    return output


cache = build_cache(data)
names = cache.keys()
t = build_trie(names)
pre = "An"
# print(autocomplete(t, cache, pre))
t.build_cache()















