from collections import deque


class Record():
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node():
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = deque()

    def __str__(self):
        return "id: " + str(self.node_id) + "\n\tchildren: " + str([str(child.node_id) for child in self.children])


def BuildTree(records):
    # If there are no records, return None
    if not records:
        return None

    records.sort(key=lambda x: x.record_id)

    tree = [Node(record.record_id) for record in records]

    root_record = records[0]

    if not (root_record.record_id == 0 == root_record.parent_id):
        raise ValueError("Invalid root record")

    for i in range(len(records) - 1, 0, -1):
        record = records[i]

        if record.record_id < record.parent_id:
            raise ValueError("record_id: " + str(record.record_id) + " is less than parent_id: " + str(record.parent_id))
        elif i != record.record_id:
            raise ValueError("Missing record")
        elif record.record_id == record.parent_id:
            raise ValueError("record_id: " + str(record.record_id) + " has the same parent_id")

        last_node = tree.pop()

        tree[record.parent_id].children.appendleft(last_node)

    if len(tree) != 1:
        raise ValueError("Records has unconnected elements")
    return tree[0]
