import random


def generate_graph(N):
    prev_1 = -1
    prev_2 = -1

    graph = []

    N = 8  # Число веришн

    for i in range(N - 1, 1, -1):
        if i % 2 == 0:
            if prev_1 == -1:
                graph.append({i + 1: (random.random(), random.random(), True)})
                prev_1 = i

            else:
                graph.append({i + 1: (random.random(), random.random(), True),
                              prev_1: (random.random(), random.random(), False)})
                prev_1 = i
        else:
            if prev_2 == -1:
                graph.append(
                    {i + 1: (random.random(), random.random(), False)})
                prev_2 = i
            else:
                graph.append(
                    {prev_2: (random.random(), random.random(), False)})

                prev_2 = i
    result = []

    first_node = {2: (random.random(), random.random(), False)}
    result.append(first_node)

    for i in range(len(graph) - 1, -1, -1):
        result.append(graph[i])
    return result
