class Node:
    def __init__(self, value, next_node: 'Node'=None, prev_node: 'Node'=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class LinkedQueue:
    def __init__(self):
        self.head = self.tail = None
        self.count = 0

    def __len__(self):
        return self.count

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next_node

    def enqueue(self, value):
        if self.count == 0:
            self.head = self.tail = Node(value=value)
        elif self.count == 1:
            self.tail = Node(value=value, prev_node=self.head)
            self.head.next_node = self.tail
        else:
            new_node = Node(value=value, prev_node=self.tail, next_node=None)
            self.tail.next_node = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise Exception('Queue is empty!')
        elif self.count == 1:
            value = self.head.value
            self.head = self.tail = None
        else:
            value = self.head.value
            self.head = self.head.next_node
        self.count -= 1
        return value

class BoundableObject:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.mid_x = x1 + (self.width//2)
        self.mid_y = y1 + (self.height//2)

    def __repr__(self):
        return '{x1} {y1} {x2} {y2}'.format(x1=self.x1, y1=self.y1, x2=self.x2, y2=self.y2)

    def intersects(self, other):
        return (self.x1 <= other.x2
                and other.x1 <= self.x2
                and self.y1 >= other.y2
                and other.y1 >= self.y2)

    def overlaps(self, other):
        return (self.x2 <= other.x2
                and self.x1 >= other.x1
                and self.y2 <= other.y2
                and self.y1 >= other.y1)

logs_c, queries = [int(p) for p in input().split()]

graph = {}
logs = []
# save logs
for i in range(logs_c):
    ax, ay, bx, by = [int(p) for p in input().split()]
    logs.append((i+1, BoundableObject(ax, ay, bx, by)))


# build graph
for idx, log_pair in enumerate(logs):
    # print(lo)
    log1_key, log = log_pair
    for idx_2 in range(idx+1, len(logs)):
        log2_key, log_2 = logs[idx_2]
        if log.intersects(log_2):
            # add to graph
            if log1_key not in graph:
                graph[log1_key] = []
            if log2_key not in graph:
                graph[log2_key] = []
            graph[log1_key].append(log2_key)
            graph[log2_key].append(log1_key)

# print(graph)
def get_component(graph, start_node, searched_node):
    visited = set()

    st = LinkedQueue()
    st.enqueue(start_node)
    while len(st) > 0:
        node = st.dequeue()
        if node == searched_node:
            return True
        if node in graph:
            for child in graph[node]:
                if child not in visited:
                    st.enqueue(child)
                    visited.add(child)

    return False
for _ in range(queries):
    start_node, end_node = [int(p) for p in input().split()]
    print('YES' if get_component(graph, start_node, end_node) else 'NO')

