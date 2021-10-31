from typing import Tuple, List, Dict
from dijkstra import shortestPath


# тестовые данные False - Дуга горизонтально направлена , True -  вертикально
test_graph = [
    # {1:(0,0, False)},#S #0
    {2: (5, 3, False)},  # 1
    {3: (7, 5, False), 5: (6, 6, True)},  # 2
    {4: (4, 4, False), 6: (5, 0, True)},  # 3
    {7: (3, 8, True)},  # 4
    {6: (1, 7, False), 8: (3, 3, True)},  # 5
    {9: (5, 2, True)},  # 6
    {6: (4, 5, False), 10: (8, 4, True)},  # 7
    {9: (7, 0, False)},  # 8
    {10: (2, 0, False)},  # 9
    {11: (1, 0, False)},  # 10
    # {"T": (0,0,False)} #11
]

test_graph_2 = [
    # 0: {1:(0,0,False)}
    {2: (1, 3, False)},  # 1
    {6: (3, 3, False), 3: (2, 3, True)},  # 2
    {4: (2, 3, False)},  # 3
    {8: (4, 3, False)},  # 4
    {7: (6, 3, False), 4: (2, 3, True)},  # 5
    {5: (1, 3, False)},  # 6
    {8: (3, 3, True)},  # 7
    # {T: (0,0, False)}

]


def get_num_arcs(graph: List[Dict[int, Tuple[int, int, bool]]]) -> int:
    '''Получить число ребер в новой сети'''

    count = 0
    for i in graph:
        for j in i.items():
            count += 1
    return count


def get_num_arc(graph: List[Dict[int, Tuple[int, int, bool]]], num_line: int, num_row: int) -> int:
    '''получить порядковый номер ребра в сети (номер метки L)'''
    count = 0
    for index, node in enumerate(graph):
        for row, _ in enumerate(node):
            count += 1
            if index == num_line and row == num_row:
                return count - 1


def restore_path(graph:  List[Dict[int, Tuple[int, int, bool]]], path: List[int]) -> List:
    '''Восстанвилваем исходный путь'''
    result_path = []
    index_path = 0
    for index_line, node in enumerate(graph):
        index_row = 0
        for k, _ in node.items():
            if path[index_path] == get_num_arc(graph, index_line, index_row):
                result_path.append(index_line)
                
                
                index_path += 1
            index_row += 1
    result_path.pop(0)
    return result_path


def build_fake_graph(graph: List[Dict[int, Tuple[int, int, bool]]]) -> List[Dict[int, int]]:
    '''Строим фиктивную сеть'''
    num_fake_nods = get_num_arcs(graph)
    fake_graph = [dict() for i in range(num_fake_nods)]

    input = 0
    for index, node in enumerate(graph):
        for key, value in node.items():
            if key == "T":
                return fake_graph
            next_node = graph[key]
            row = 0
            for _, need in next_node.items():
                if ((need[2] + value[2]) % 2) == 0:
                    coast = value[0]

                else:
                    coast = value[0] + value[1]
                output = get_num_arc(graph, key, row)
                fake_graph[input][output] = coast
                row += 1
            input += 1


def print_fake_graph(graph: List[Dict[int, int]]) -> None:
    '''Вывод фейкового графа'''
    index_last = len(graph) - 1
    for i, node in enumerate(graph):
        if i == 0:
            print(f"S:{node}")
        elif i == index_last:
            print(f"T")
        else:
            print(f"L{i}: {node}")


def print_graph(graph: List[Dict[int, int]]) -> None:
    '''Вывод графа'''
    for i, node in enumerate(graph):
        print(f"{i + 1}: {node}")


def add_fake_nodes(graph: List[Dict[int, Tuple[int, int, bool]]]) -> List[Dict[int, Tuple[int, int, bool]]]:
    '''Добавляем фиктивные узлы'''
    g = graph.copy()
    g.append({"T": (0, 0, False)})
    S1 = {1: (0, 0, False)}
    g.insert(0, S1)
    return g

def generate_graph(num_vertex:int):
    '''Генерирует граф'''
    graph = []
    if num_vertex % 2 == 0:
        pass
    else:
        


def main(graph) -> None:
    '''Запуск программы с тестовыми данными'''
    print("Graph")
    print_graph(graph)
    graph = add_fake_nodes(graph)
    fake_graph = build_fake_graph(graph)
    print("Fake network")
    print_fake_graph(fake_graph)
    final_vertex = len(fake_graph) - 1
    result, distances = shortestPath(fake_graph, 0, final_vertex)
    result = restore_path(graph, result)
    print(f"Path:{result}")
    print(f"Coast:{distances[final_vertex]}")



if __name__ == "__main__":
    main(test_graph_2)
