#  https://www.hackerrank.com/contests/juniper-hackathon/challenges/friend-circles


def traverse_friend_circle(node: int, friends: [[int]]) -> set:
    """
    Given a starting node, go through all of his friends and their friends and their and etc...,
        while storing each node
    """
    from collections import deque

    friend_circle = {node}
    friends_to_visit = deque()
    friends_to_visit.append(node)

    while friends_to_visit:
        node = friends_to_visit.popleft()

        for friend, are_friends in enumerate(friends[node]):
            if are_friends and friend not in friend_circle:
                friend_circle.add(friend)
                friends_to_visit.append(friend)

    return friend_circle


CONNECTION_TO_BOOL = {
    'Y': True,
    'N': False
}
n = int(input())
# Build a boolean matrix
matrix = []
for _ in range(n):
    matrix.append([CONNECTION_TO_BOOL[conn] for conn in input()])

# the number of friend circles is the number of components in the graph

visited = set()
friend_circle_count = 0
for node in range(n):
    if node not in visited:
        friend_circle: {int} = traverse_friend_circle(node, matrix)
        visited.update(friend_circle)
        friend_circle_count += 1

print(friend_circle_count)
