
class Node:
    def __init__(self, value, parent, xor_count, left=None, right=None):
        self.value = value
        self.xor_count = xor_count
        self.parent = parent
        self.left = left
        self.right = right
        self.balance_factor = 0
        self.index = 0

    def __iter__(self):
        if self.left is not None:
            yield from self.left.__iter__()
        yield self.value
        if self.right is not None:
            yield from self.right.__iter__()

    def __repr__(self):
        return 'Node {val} with BF {bf}'.format(val=self.value, bf=self.balance_factor)

    def print_node(self, tab=0):
        if self.right is not None:
            self.right.print_node(tab+2)
        print((' '*tab) + str(self.value))
        if self.left is not None:
            self.left.print_node(tab+2)


class AvlTree:
    # TODO: REFACTOR!
    def __init__(self):
        self.root = None
        self.count = 0

    def __len__(self):
        return self.count

    def __iter__(self):
        yield from self.root.__iter__()

    def __getitem__(self, index):
        # some pathetic support for negative indexing
        if index < 0:
            index += self.count

        def get_node(node):
            if index == node.index:
                return node
            elif index < node.index:
                if node.left is not None:
                    return get_node(node.left)
                else:
                    return None
            else:
                if node.right is not None:
                    return get_node(node.right)
                else:
                    return None
        node = get_node(self.root)
        if node is not None:
            return node.value

    def print_tree(self):
        if self.root is not None:
            self.root.print_node()

    def add(self, value, xor_value):
        if self.root is None:
            self.root = Node(value=value, xor_count=xor_value, parent=None)
            self.count += 1
            return
        parent, direction = self._find_parent(value)
        if parent is None:
            return  # value is already in the tree
        new_node = Node(value=value, xor_count=xor_value, parent=parent)
        if direction == 'L':
            parent.left = new_node
        else:
            parent.right = new_node
        self.modify_balance_factor(new_node)
        self.update_indexes()
        self.count += 1

    def modify_balance_factor(self, node):
        """ Modifies the balance factor for each node upwards of the given one"""
        parent = node.parent
        if parent is None:
            return
        direction = 'L' if parent.value > node.value else 'R'
        if direction == 'L':
            parent.balance_factor += 1
        else:
            parent.balance_factor += -1
        if parent.balance_factor != 0:
            if parent.balance_factor in [-2, 2]:
                # TODO: ROTATE :)
                if parent.balance_factor == -2:
                    parent_dir = 'R'
                    if node.balance_factor == -1:
                        node_dir = 'R'
                    else:
                        node_dir = 'L'
                    general_dir = node_dir + parent_dir
                    if general_dir == 'RR':
                        self.left_rotation(node=node, parent=parent)
                    elif general_dir == 'LR':
                        # TODO: RIGHT-LEFT ROTATION
                        self.right_rotation(node.left, node)
                        self.left_rotation(node.parent, parent)

                    else:
                        raise Exception('Unexpected behavior!')
                else:
                    parent_dir = 'L'
                    if node.balance_factor == -1:
                        node_dir = 'R'
                    else:
                        node_dir = 'L'
                    general_dir = node_dir + parent_dir
                    if general_dir == 'LL':
                        self.right_rotation(node, parent)
                    elif general_dir == 'RL':
                        # TODO: LEFT-RIGHT ROTATION
                        self.left_rotation(node.right, node)
                        self.right_rotation(node.parent, parent)
                    else:
                        raise Exception('Unexpected behavior!')
            else:
                self.modify_balance_factor(parent)

    def left_rotation(self, node: Node, parent: Node):
        grand_parent = parent.parent
        old_left = node.left
        node.left = parent
        parent.right = old_left
        if old_left is not None:
            old_left.parent = parent
        parent.parent = node
        node.parent = grand_parent
        if grand_parent is None:
            self.root = node
        else:
            if grand_parent.value > node.value:
                grand_parent.left = node
            else:
                grand_parent.right = node
        parent.balance_factor = 0
        node.balance_factor = 0

    def right_rotation(self, node: Node, parent: Node):
        grand_parent = parent.parent
        old_right = node.right
        node.right = parent
        parent.left = old_right
        if old_right is not None:
            old_right.parent = parent
        parent.parent = node
        node.parent = grand_parent
        if grand_parent is None:
            self.root = node
        else:
            if grand_parent.value > node.value:
                grand_parent.left = node
            else:
                grand_parent.right = node
        parent.balance_factor = 0
        node.balance_factor = 0

    def _find_parent(self, value):
        """ Find the appropriate parent for a newly-added value """
        def _find(root: Node):
            if root.value == value:
                return None, None  # value is already in the tree
            if root.value > value:
                if root.left is not None:
                    return _find(root.left)
                else:
                    return root, 'L'
            else:
                if root.right is not None:
                    return _find(root.right)
                else:
                    return root, 'R'

        return _find(self.root)

    def get_item(self, value):
        def dfs(node):
            if node.value == value:
                return node
            elif node.value > value:
                return dfs(node.left)
            elif node.value < value:
                return dfs(node.right)
        return dfs(self.root)

    def get_closest_element(self, value):
        closest_val = 0
        closest_node = self.root
        def dfs(node):
            nonlocal closest_val, closest_node
            if node.value == value:
                raise Exception()
            if node.value < value:
                if node.value > closest_val:
                    closest_val = node.value
                    closest_node = node
                if node.right is not None:
                    dfs(node.right)
            elif node.value > value and node.left is not None:
                dfs(node.left)
        dfs(self.root)
        return closest_node



    def update_indexes(self):
        """ Go through the whole tree in-order and modify the indexes of each node """
        index = 0

        def update_index(node):
            nonlocal index
            if node.left is not None:
                update_index(node.left)
            node.index = index
            index += 1
            if node.right is not None:
                update_index(node.right)
        update_index(self.root)

    def range(self, start, end):
        items = []
        if self.root is None:
            return []

        def in_order_dfs(node):
            nonlocal items
            if node.value > start and node.left is not None:
                in_order_dfs(node.left)
            if end >= node.value >= start:
                items.append(node.value)
            if node.value < end and node.right is not None:
                in_order_dfs(node.right)

        in_order_dfs(self.root)
        return items


def main():
    saved_x = AvlTree()
    saved_x.add(1, 0)
    saved_x.add(3, 0)
    x_in_tree = {1, 3}
    max = 10 ** 10
    i = 3
    while i <= max:
        i *= 2
        i += 1
        saved_x.add(i, 0)
        x_in_tree.add(i)

    fast_saved_x = {1: 0, 2: 1, 3: 0}
    old_value = 3
    for i in range(4, (10 ** 4) + 1):
        if old_value == -1:
            old_value = i - 1
        fast_saved_x[i] = old_value
        old_value -= 1

    query_count = int(input())
    for _ in range(query_count):
        x = int(input())
        if x in x_in_tree:
            print(0)
        elif x in fast_saved_x:
            print(fast_saved_x[x])
        else:
            # get closest value
            closest_x = saved_x.get_closest_element(x).value
            diff = x - closest_x
            print(closest_x-diff+1)


if __name__ == '__main__':
    main()
