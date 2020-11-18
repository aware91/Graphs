from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):
    parent_dictionary = defaultdict(list)
    
    for pair in ancestors:
        parent_dictionary[pair[1]].append(pair[0])
        print(pair[0], pair[1], "Pair", pair, dict.__repr__(parent_dictionary))

    if starting_node not in parent_dictionary:
        return -1

    def recursive_ancestor(child, level=0):
        print(f"\n recurs -- child: {child} {parent_dictionary}")
        if child not in parent_dictionary:
            print(f"\n child not in parent dictionary, append to list",
                (child, level),"\n")
            return (child, level)
        else:
            candidates = []
            for parent in parent_dictionary[child]:
                print(
                    candidates,
                    level,
                    child,
                    "< ---Child Parent--- >",
                    parent,
                    parent_dictionary[child],
                    "Candidates")
                candidates.append(recursive_ancestor(parent, level + 1))
            print("Return Sorted", child, "<-Child Level->", level, candidates)
            return sorted(candidates, key=lambda x: (x[1]), reverse=True)[0]
    return recursive_ancestor(starting_node)[0]


# Mari's code for this
"""
Understand
Plan
    1. Translate the problem into graph terminology
        Vertex - user
        edge - parent-child relationship between two users
        weights - N/A
        path - a user's family tree

    2. Build your Graph (if needed)
        build graph based on edges we're given, each user has a directed edge to its ancestor/parent

    3. Traverse the graph
        traverse all paths starting from starting_node, keep track of tarthest node found with the lowest user id
        simply output that node
"""
# from collections import deque
# from collections import defaultdict

# def earliest_ancestor(ancestors, starting_node):
#     graph = createGraph(ancestors)
#     earlistAncestor = (starting_node, 0)
#     stack = deque()
#     stack.append((starting_node, 0))
#     visited = set()
#     while len(stack) > 0:
#         curr = stack.pop()
#         currNode, distance = curr[0], curr[1]
#         visited.add(curr)
        
#         if currNode not in graph:
#             if distance > earlistAncestor[1]:
#                 earlistAncestor = curr
#             elif distance == earlistAncestor[1] and currNode < earlistAncestor[0]:
#                 earlistAncestor = curr
        
#         else:
#             for ancestor in graph[currNode]:
#                 if ancestor not in visited:
#                     stack.append((ancestor, distance + 1))
    
#     return earlistAncestor[0] if earlistAncestor[0] != starting_node else -1

# def createGraph(edges):
#     graph = defaultdict(set)
#     for edge in edges:
#         ancestor, child = edge[0], edge[1]
#         graph[child].add(ancestor)
#     return graph