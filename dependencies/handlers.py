from .enums import cutoff, failure
from .node import Node


def expand(problem, node):
    """
    Раскрываем узел, создавая дочерние узлы.

    :param problem: Проблема, для которой выполняется поиск
     (должна иметь методы actions, result и action_cost).
    :param node: Узел, который нужно раскрыть.
    :yield: Дочерние узлы.
    """
    s = node.state
    for action in problem.actions(s):
        s1 = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s1)
        yield Node(s1, node, action, cost)


def path_actions(node):
    """
    Возвращает последовательность действий, чтобы добраться до указанного узла.

    :param node: Узел, для которого нужно получить последовательность действий.
    :return: Список действий.
    """
    if node is None or node.parent is None:
        return []
    return path_actions(node.parent) + [node.action]


def path_states(node):
    """
    Возвращает последовательность состояний, чтобы добраться до
    указанного узла.

    :param node: Узел, для которого нужно получить последовательность
     состояний.
    :return: Список состояний.
    """
    if node in (cutoff, failure, None):
        return []
    return path_states(node.parent) + [node.state]  # type: ignore[union-attr]
