import heapq
import networkx as nx
import matplotlib.pyplot as plt

def a_star(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path, g

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(
                    open_list,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, float('inf')


graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('D', 5), ('E', 9)],
    'C': [('F', 3)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

start = 'A'
goal = 'G'

print("GRAPH")
print("-" * 30)

for node in graph:
    for neighbor, cost in graph[node]:
        print(f"{node} -> {neighbor} : Cost = {cost}")

print("\nHEURISTIC VALUES")
print("-" * 30)

for node, value in heuristic.items():
    print(f"h({node}) = {value}")

path, cost = a_star(graph, heuristic, start, goal)

print("\nRESULT")
print("-" * 30)
print(f"Start Node : {start}")
print(f"Goal Node  : {goal}")
print(f"Shortest Path : {' -> '.join(path)}")
print(f"Total Cost : {cost}")


G = nx.DiGraph()

for node in graph:
    for neighbor, cost in graph[node]:
        G.add_edge(node, neighbor, weight=cost)

pos = {
    'A': (0, 2),
    'B': (2, 3),
    'C': (2, 1),
    'D': (4, 3),
    'E': (4, 1),
    'F': (4, 0),
    'G': (6, 2)
}

plt.figure(figsize=(10, 6))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    font_size=12,
    arrows=True
)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=edge_labels,
    font_size=11
)

plt.title("A* Search Graph")
plt.axis("off")
plt.show()
