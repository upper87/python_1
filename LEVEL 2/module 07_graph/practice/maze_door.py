def dfs(graph, start_vertex):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start_vertex)
    return visited


def bfs(graph, start_vertex):
    lengths = [None] * len(graph)
    lengths[start_vertex] = 0
    queue = [start_vertex]

    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths

def is_find_key(graph: list, start_point: int, keys: list) -> bool:
    visited = dfs(graph, start_point)
    for key in keys:
        if visited[key]:
            return True
    return False


maze_with_door = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]

maze_without_door = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8, 5],  # 4
    [1, 4],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [9, 6],  # 10
    [7, 15],  # 11
    [8, 13],  # 12
    [12],  # 13
    [15],  # 14
    [11, 14],  # 15
]

# start_point1 = 5
# start_point2 = 13
# start_point3 = 3
# start_point4 = 8
finish_point = 0

start_points = {
    "s1": 5,
    "s2": 13,
    "s3": 3,
    "s4": 8,
}
keys = [7, 10]

visited = dfs(maze_with_door, finish_point)

for point_name, point_position in start_points.items():
    if visited[point_position]: # Дойдем без ключа
        print(f"Из точки {point_name} можно добраться до финиша без ключа")
    else: # Ищем ключ
        if is_find_key(maze_with_door, point_position, keys):
            visited_open = dfs(maze_without_door, finish_point)
            if visited_open[point_position]:
                print(f"Из точки {point_name} можно добраться до финиша c ключом")
            else:
                print(f"Из точки {point_name} нельзя добраться до финиша")
        else:
            print(f"Из точки {point_name} нельзя добраться до финиша")
