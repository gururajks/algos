"""
Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID. 

The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

Example:
logs = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["215", "user_6", "resource_4"],
    ["200", "user_6", "resource_5"],    
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_4", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_2"],
    ["54359", "user_1", "resource_3"],
]

Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency list with probabilities. Add __START__ and __END__ states.

Specifically, for each resource, we want to compute a list of every possible next step taken by any user, together with the corresponding probabilities. The list of resources should include __START__ but not __END__, since by definition __END__ is a terminal state.

Answer:
{'__START__': {'resource_3': 0.5, 'resource_2': 0.25, 'resource_1': 0.25}, 
 'resource_1': {'resource_6': 0.333, '__END__': 0.667},
 'resource_2': {'__END__': 1.0}, 
 'resource_3': {'__END__': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},  
 'resource_4': {'__END__': 1.0}, 
 'resource_5': {'resource_4': 1.0}, 
 'resource_6': {'resource_5': 1.0}, 
}

For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 2 users have resource_1 as a first visit (user_4, user_6), and 2 users have resource_2 as a first visit (user_7, user_8) so the possible next steps for __START__ are resource_3 with probability 4/8, resource_1 with probability 2/8, and resource_2 with probability 2/8.


(These are the resource paths per user, ordered by access time:
{
'user_1': ['resource_3', 'resource_3', 'resource_1'], 
'user_2': ['resource_3', 'resource_2'], 
'user_3': ['resource_3'],
'user_4': ['resource_1'],
'user_5': ['resource_3'], 

'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'], 
'user_7': ['resource_2'],
'user_8': ['resource_2'],
}
)

Complexity analysis variables:

n: number of logs in the input

"""

from collections import defaultdict
from pprint import pprint

def get_transition_prob(logs):
    arr = build_graph(logs)
#     pprint(arr)
    count_graph = defaultdict(dict)
    for k, v in arr.items():

        if '__START__' in count_graph and v[0] in count_graph['__START__']:
            count_graph['__START__'][v[0]] += 1
        else:
            count_graph['__START__'].update({v[0] : 1})

        idx = 0
        while idx + 1 < len(v):
            fro = v[idx]
            to = v[idx + 1]

            # r3 : {r1 : 1, r3: 2},
            if fro in count_graph and to in count_graph[fro]:
                count_graph[fro][to] += 1
            else:
                count_graph[fro].update({to : 1})
            idx += 1

        if v[idx] in count_graph and '__END__' in count_graph[v[idx]]:
            count_graph[v[idx]]['__END__'] +=1
        else:
            count_graph[v[idx]].update({'__END__' : 1})

    output = defaultdict(dict)
    for k, v in count_graph.items():

        total = sum(v.values())
        for r, count in v.items():
            output[k].update({r : count / total})

    return output


def build_graph(logs):

    graph = defaultdict(list)
    for time, user, resource in logs:
        graph[user].append((resource, int(time)))

    output = defaultdict(list)
    for k, v in graph.items():
        dup_v = sorted(v, key = lambda x : x[1])
        for r, t in dup_v:
            output[k].append(r)

    return output



logs = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_4", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_2"],
[ "54359", "user_1", "resource_3"],
]

a = get_transition_prob(logs)
pprint(a)






































from collections import defaultdict


def resource_access(init_arr):
    arr = sorted(init_arr, key = lambda x : int(x[0]))

    left, right = 0, 0
    hMap = defaultdict(int)
    max_hMap = {}
    time_entry = {}
    max_resource_time = 0
    max_resource = ""
    while right < len(arr):
        end_time, user, resource = arr[right]
        end_time = int(end_time)

        hMap[resource] += 1
        begin_time , begin_user, begin_resource = arr[left]
        while int(begin_time) < end_time - 300:
            hMap[begin_resource] -= 1
            if hMap[begin_resource] == 0:
                del hMap[begin_resource]
            left += 1
            begin_time , begin_user, begin_resource = arr[left]

        max_hMap[resource] = max(hMap[resource], max_hMap.get(resource, 0))

        if max_resource_time < max_hMap[resource]:
            max_resource_time = max_hMap[resource]
            max_resource = resource

        right += 1

    return max_resource, max_resource_time



































def get_min_max_user(arr):

    if not arr:
        return
    hMap = defaultdict(list)
    for time, user, resource in arr:
        time = int(time)
        if user in hMap:
            min_time, max_time = hMap[user]
            hMap[user] = [min(min_time, time), max(max_time, time)]
        else:
            hMap[user] = [time, time]

    return hMap

