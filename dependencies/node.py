class Node:
    "Узел в дереве поиска"

    def __init__(self, state, parent=None, action=None, path_cost=0.0) -> None:
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return "<{}>".format(self.state)

    def __len__(self):
        return 0 if self.parent is None else (1 + len(self.parent))

    def __lt__(self, other) -> bool:
        return self.path_cost < other.path_cost
