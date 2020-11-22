import os, json
import collections


def find_path_dfs(g, s, d):
    visited = set()

    def keep_track(g, curr, dest, crumbs):
        if curr == dest:
            print("dfs {}".format(crumbs))
            return
        visited.add(curr)
        for v in g[curr]:
            if v not in visited:
                crumb.append(v)
                keep_track(g, v, dest, crumb)
                crumb.pop()

    crumb = [s]
    keep_track(g, s, d, crumb)


def find_path_bfs(g, s, dest):
    from collections import deque

    def print_path(p, v, crumbs):
        if v == -1:
            crumbs.reverse()
            print("bfs: {}".format(crumbs))
            return
        crumbs.append(v)
        print_path(p, p[v], crumbs)

    parent = {}
    q = deque()
    q.append(s)
    visited = set()
    visited.add(s)
    parent[s] = -1
    while len(q) > 0:
        curr = q.popleft()
        if curr == dest:
            crumbs = []
            print_path(parent, curr, crumbs)
            break
        for v in g[curr]:
            if v not in visited:
                q.append(v)
                visited.add(v)
                parent[v] = curr


def fix_graph(g):
    for k, v in g.items():
        for vertex in v:
            if k not in g[vertex]:
                g[vertex].append(k)


if __name__ == "__main__":
    g = {
        1: [2, 5, 6, 7, 8],
        2: [1, 5, 3, 7],
        3: [2, 4],
        4: [3, 5, 7],
        5: [1, 2, 4],
        6: [1, 7, 8, 9],
        7: [2, 4, 1, 6, 8],
        8: [1, 6, 7],
        9: [6]
    }
    # fix_graph(g)

    find_path_dfs(g, 2, 9)
    find_path_bfs(g, 2, 8)
