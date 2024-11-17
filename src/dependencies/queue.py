import heapq
from collections import deque

# FIFOQueue: очередь с поведением FIFO (first-in, first-out).
FIFOQueue = deque

# LIFOQueue: очередь с поведением LIFO (last-in, first-out).
LIFOQueue = list


class PriorityQueue:
    """Очередь, в которой элемент с минимальным значением f(item) всегда
    выгружается первым."""

    def __init__(self, items=(), key=lambda x: x):
        """
        Инициализирует приоритетную очередь.

        :param items: Итерация элементов для добавления в очередь.
        :param key: Функция для вычисления приоритетов.
        """
        self.key = key
        self.items = []
        for item in items:
            self.add(item)

    def add(self, item):
        """
        Добавляет элемент в очередь.

        :param item: Элемент для добавления.
        """
        pair = (self.key(item), item)
        heapq.heappush(self.items, pair)

    def pop(self):
        """
        Удаляет и возвращает элемент с минимальным значением f(item).

        :return: Элемент с минимальным приоритетом.
        """
        return heapq.heappop(self.items)[1]

    def top(self):
        """
        Возвращает элемент с минимальным значением f(item), не удаляя его.

        :return: Элемент с минимальным приоритетом.
        """
        return self.items[0][1]

    def __len__(self):
        """
        Возвращает количество элементов в очереди.

        :return: Количество элементов.
        """
        return len(self.items)
