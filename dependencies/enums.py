import math

from .node import Node

# Алгоритм не смог найти решение.
failure = Node("failure", path_cost=math.inf)

# Указывает на то, что поиск с итеративным углублением был прерван.
cutoff = Node("cutoff", path_cost=math.inf)
