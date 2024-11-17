#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Для задачи "Расширенный подсчет количества островов в бинарной матрице"
# подготовить собственную матрицу, для которой с помощью разработанной в
# предыдущем пункте программы, подсчитать количество островов.


from dependencies import FIFOQueue

# Матрица 10x10
grid = [
    [1, 1, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    [1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
]


class IslandCountingProblem:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def actions(self, state):
        """Возвращает возможные соседние клетки (включая диагонали)"""
        row, col = state
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),  # горизонтальные и вертикальные
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1),  # диагонали
        ]
        valid_actions = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                if self.grid[new_row][new_col] == 1:  # Соседняя клетка земля
                    valid_actions.append((new_row, new_col))
        return valid_actions

    def result(self, state, action):
        """Возвращает новое состояние (соседнюю клетку)"""
        return action

    def is_goal(self, state):
        """Для задачи подсчета островов не требуется использовать цель"""
        return False

    def action_cost(self, s, a, s1):
        """Все переходы стоят одинаково"""
        return 1

    def h(self, node):
        """Оценка не требуется, так как
        задача не ориентирована на поиск
        """
        return 0


def count_islands(grid):
    problem = IslandCountingProblem(grid)
    visited = set()
    island_count = 0

    # Проходим по всем клеткам
    for row in range(problem.rows):
        for col in range(problem.cols):
            if grid[row][col] == 1 and (row, col) not in visited:
                # Запускаем BFS, чтобы посетить все клетки острова
                island_count += 1
                print(
                    f"Новый остров найден, начинаем с клетки: ({row}, {col})"
                )  # Отладочный вывод
                # Запуск BFS для каждого нового острова
                bfs(problem, (row, col), visited)

    return island_count


def bfs(problem, start, visited):
    queue = FIFOQueue([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        for neighbor in problem.actions(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


if __name__ == "__main__":
    # Подсчитываем количество островов
    island_count = count_islands(grid)
    print(f"Количество островов: {island_count}")
