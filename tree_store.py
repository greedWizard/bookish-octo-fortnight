from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    id: int
    type: str
    children: list['Node'] = field(default_factory=list)
    parent_id: int | None = None

    def __repr__(self) -> str:
        return f'<Node id: {self.id}, parent_id: ' \
                f'{self.parent_id} type: "{self.type}">'

    def __str__(self) -> str:
        return f'Node id: {self.id}, parent_id: ' \
                f'{self.parent_id} type: "{self.type}" children: {self.children}'


class TreeStore:
    def __init__(self, items: list[list[dict[str, Any]]] = None) -> None:
        if not items:
            items = []

        # будем хранить элементы в dict'е, т.к брать элементы по индексу
        # будет очень быстро (O(1)) и удобно
        self.nodes_map = {item['id']: Node(**item) for item in items}

        self._set_parents()

    def _set_parents(self) -> None:
        for node in self.nodes_map.values():
            if node.parent_id:
                self.nodes_map[node.parent_id].children.append(node)
        
    def get_all(self):
        return [value for value in self.nodes_map.values()]

    def get_item(self, id: int) -> Node:
        return self.nodes_map.get(id)

    def get_children(self, parent_id: int) -> list[Node]:
        item = self.get_item(parent_id)
        return item.children if item else []

    def get_all_parents(self, child_id: int) -> list[Node]:
        child = self.get_item(child_id)
        parents = []


        if child:
            while child.parent_id:
                parent = self.get_item(child.parent_id)
                parents.append(parent)
                child = parent
        return parents
