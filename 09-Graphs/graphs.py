# Adjacency List vs. Adjacency Matrix
# An adjacency list looks like this:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
# An adjacency matrix looks like this:
# graph_matrix = [[0, 1, 1, 0, 0, 0],  # A
#                 [1, 0, 0, 1, 1, 0],  # B
#                 [1, 0, 0, 0, 0, 1],  # C
#                 [0, 1, 0, 0, 0, 0],  # D
#                 [0, 1, 0, 0, 0, 1],  # E
#                 [0, 0, 1, 0, 1, 0]]  # F
# A matrix is filled with 0s and 1s. If there is an edge between vertices i and j, then the cell at the
# i-th row and j-th column (matrix[i][j]) will be 1, otherwise, it will be 0.
# The adjacency matrix is easier to implement and perform lookups, but it consumes more space.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self):
        pass

    def add_edge(self):
        pass

    def remove_edge(self):
        pass
