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

    # Sort the records by id
    records.sort(key=lambda x: x.record_id)

    # Create nodes with empty children for each record
    node_list = [Node(record.record_id) for record in records]

    # Get the root record
    root_record = records[0]

    # Make sure that the root record has zero for both record_id and parent_id
    if not (root_record.record_id == 0 == root_record.parent_id):
        raise ValueError("Invalid root record")

    # Loop through the nodes in reverse
    for i in range(len(records) - 1, 0, -1):
        record = records[i]

        # Checks to ensure that each record is valid
        if record.record_id < record.parent_id:
            raise ValueError("record_id: " + str(record.record_id) + " is less than parent_id: " + str(record.parent_id))
        elif i != record.record_id:
            raise ValueError("Missing record")
        elif record.record_id == record.parent_id:
            raise ValueError("record_id: " + str(record.record_id) + " has the same parent_id")

        # Get the final element of the initialized nodes
        last_node = node_list.pop()

        # Append the most recent node to its corresponding parent
        node_list[record.parent_id].children.appendleft(last_node)

    # Raise an error if there are any other nodes remaining apart from
    # the root node
    if len(node_list) != 1:
        raise ValueError("Records has unconnected elements")
    # Otherwise, return the root node, which is its first element
    return node_list[0]
