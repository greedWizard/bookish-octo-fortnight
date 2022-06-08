import json

from tree_store import TreeStore


def main():
    try:
        with open('data.json', 'rt') as data_file:
            raw_data = json.load(data_file)
    except FileNotFoundError:
        print('Файл data.json не найден')
        return

    tree_store = TreeStore(raw_data)
    
    item_id = 1
    first_item = tree_store.get_item(item_id)
    assert first_item.id == item_id, first_item
    print(f'{first_item=}')
    
    print()

    first_children = tree_store.get_children(item_id)
    # считаем сколько объектов с таким parent_id было в исходном словаре
    actual_children = [raw_node for raw_node in raw_data if raw_node['parent_id'] == item_id]
    assert len(first_children) == len(actual_children), first_children
    print(f'{first_children=}')

    print()

    lowest_node_id = 6
    all_parents = tree_store.get_all_parents(lowest_node_id)
    assert len(all_parents) == 3, all_parents
    print(f'parents for {lowest_node_id}: {all_parents}')


if __name__ == '__main__':
    main()