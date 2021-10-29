from priodict import priorityDictionary
from typing import Tuple, Dict, List


def Dijkstra(G, start: int, end: int = None) -> Tuple[Dict, Dict]:
    '''Модифицированный алгоритм Дейкстра для нахождения кратчайшего пути
     использующий словарь с приоритетом. Вовзращает словарь конечных весов до вершин
     и словарь предшественников вершин для востановления пути'''

    D = {}  # Словарь конечных весов до вершин
    P = {}  # словарь предшественников
    Q = priorityDictionary()
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        if v == end:
            break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError(
                        "Дейкстра: уже найден лучший путь к конечной вершине")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


def shortestPath(G, start: int, end: int) -> Tuple[List, Dict]:
    """Находит короткий путь, и список с минимальной стоимость для каждой вершины"""

    D, P = Dijkstra(G, start, end)
    Path = []
    while True:
        Path.append(end)
        if end == start:
            break
        end = P[end]
    Path.reverse()
    return (Path, D)
