from typing import Tuple, List, Dict
import re


def get_dict_adj(input_nodes: str) -> Dict[int, Tuple[int, int, bool]]:
    '''Функция возвращает словарь инцедентных вершиш вместе с их платой за перемещение в них, штрафом за поворот
    и булевым значением выполняется ли штраф за вхождение в эту вершину'''
    result = {}
    if input_nodes == "":
        return result
    pattern = r"(\(\d+,\d+,[10]\)){1,2}"
    matched_nodes = re.match(pattern, input_nodes)
    if not matched_nodes:
        raise ValueError("Неверно введены данные")
    else:
        res = matched_nodes.group(0)
        parsed_data = [arc.replace('(', '').replace(')', '')
                       for arc in res.split(")(")]
        for arc in parsed_data:
            buf = [int(j) for j in arc.split(',')]
            buf[2] = bool(buf[2])
            result[buf[0]] = (buf[1], buf[2])
    return result


# тестовые данные
test_graph = [
    # {1:(0,0)},#S #0
    {2: (5, 3, False)},  # 1
    {3: (7, 5, False), 5: (6, 6, True)},  # 2
    {4: (4, 4, False), 6: (5, 0, True)},  # 3
    {7: (3, 8, True)},  # 4
    {6: (1, 7, True), 8: (3, 3, False)},  # 5
    {9: (5, 2, True)},  # 6
    {6: (4, 5, True), 10: (8, 4, False)},  # 7
    {9: (7, 0, True)},  # 8
    {10: (2, 0, True)},  # 9
    {11: (1, 0, True)},  # 10
    # {"T": (0,0,True)} #11
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
                if need[2]:
                    coast = value[0] + value[1]
                else:
                    coast = value[0]
                output = get_num_arc(graph, key, row)
                fake_graph[input][output] = coast
                row += 1
            input += 1


def print_graph(graph: List[Dict[int, int]]) -> None:
    '''Вывод графа'''
    for i, node in enumerate(graph):
        print(f"{i}: {node}")


def add_fake_nodes(graph: List[Dict[int, Tuple[int, int, bool]]]) -> List[Dict[int, Tuple[int, int, bool]]]:
    '''Добавляем фиктивные узлы'''
    g = graph.copy()
    g.append({"T": (0, 0, True)})
    S1 = {1: (0, 0, True)}
    g.insert(0, S1)
    return g


def test() -> None:
    '''Запуск программы с тестовыми данными'''
    print("Graph")
    print_graph(test_graph)
    graph = add_fake_nodes(test_graph)
    fake_graph = build_fake_graph(graph)
    print("Fake network")
    print_graph(fake_graph)


def main() -> None:
    '''Запуск программы с вводом'''
    num_nodes = int(input("Введите количество вершин:"))
    print("""Введите для каждого вершины с чем она соединена
          "Номер вершины:(Номер вершины,плата,штраф за поворот из исходной вершины в эту, 1 или 0)
           1 - штрафовать за поворот по этой дуге
           0 - не штрафовать
           Пример:
           1:(2,5,0)
           2:(3,7,0)(5,6,1)
           ....
           """)
    graph = []
    for i in range(num_nodes):
        input_nodes = input(f"{i+1}:")
        graph.append(get_dict_adj(input_nodes))
        graph = add_fake_nodes(test_graph)
        fake_graph = build_fake_graph(graph)
        print("Fake network")
        print_graph(fake_graph)


if __name__ == "__main__":
    '''Раскоииентировать нужную и закоментировать ненужную'''
    # main()
    test()
