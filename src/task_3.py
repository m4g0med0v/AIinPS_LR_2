#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Для задачи "Поиск кратчайшего пути в лабиринте" подготовить собственную схему
# лабиринта, а также определить начальную и конечную позиции в лабиринте. Для
# данных данных найти минимальный путь в лабиринте от начальной к конечной
# позиции.


from dependencies import Problem, breadth_first_search, failure, path_states

# Направления для движения (вверх, вниз, влево, вправо)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class MazeProblem(Problem):
    def __init__(self, maze, initial, goal, **kwds):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])
        super().__init__(initial=initial, goal=goal, **kwds)

    def actions(self, state):
        """Возвращает доступные действия из текущего состояния"""
        x, y = state
        actions = []
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.maze[nx][ny] == 1:
                actions.append((nx, ny))  # Если клетка проходима (1)
        return actions

    def result(self, state, action):
        """Возвращает новое состояние после применения действия"""
        return action

    def is_goal(self, state):
        """Проверка, достигли ли мы цели"""
        return state == self.goal

    def action_cost(self, s, a, s1):
        """Стоимость перехода всегда 1"""
        return 1


def find_shortest_path(maze, start, goal):
    # Создаем задачу с лабиринтом
    problem = MazeProblem(maze, initial=start, goal=goal)
    solution_node = breadth_first_search(problem)

    if solution_node != failure:
        # Если решение найдено, возвращаем путь
        path = path_states(solution_node)
        return path
    else:
        # Если решения нет, возвращаем None
        return None


if __name__ == "__main__":
    # Пример лабиринта (0 — стена, 1 — путь)
    maze = [
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 1, 0, 1],
    ]

    start = (0, 0)  # Начальная точка
    goal = (7, 5)  # Конечная точка

    # Ищем кратчайший путь
    path = find_shortest_path(maze, start, goal)

    # Выводим результат
    if path:
        print(f"Кратчайший путь: {path}")
        print(f"Длина пути: {len(path) - 1}")
    else:
        print("Путь не найден.")
