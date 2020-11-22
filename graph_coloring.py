from collections import defaultdict


def feedingTime(classes):
    graph = defaultdict(list)

    for idx, single_class in enumerate(classes):
        for animal in single_class:
            graph[idx].append(animal)
            graph[animal].append(idx)

    n = len(classes)
    colors = {}
    seen = set()

    def is_safe(graph, idx):
        for child in graph[idx]:
            if colors[idx] == colors.get(child, 0):
                return False
        return True

    max_days = 0

    def graph_color(graph, idx):
        nonlocal max_days
        seen.add(idx)
        for color in range(1, n + 1):
            colors[idx] = color
            if is_safe(graph, idx):
                if len(seen) == len(graph):
                    return True
                for child in graph[idx]:
                    if child not in seen:
                        if graph_color(graph, child):
                            return True
            else:
                colors[idx] = 0
        seen.remove(idx)
        return False

    graph_color(graph, 0)
    max_days = max(colors.values())
    print(colors)
    return max_days if max_days <= 5 else -1


classes = [["Tiger", "Lima", "Frog"],
           ["Tiger", "Zebra", "Lion"],
           ["Tiger", "Rabbit"],
           ["Emu", "Zebra", "Rabbit"]]

print(feedingTime(classes))
