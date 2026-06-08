import time
import heapq
from collections import deque

# Grafo baseado na tabela de arestas do ANEXO I
# Grafo não-direcionado com pesos (distâncias em km)
graph = {
    'F': {'H': 12, 'M': 15, 'T': 18, 'J': 22, 'B': 25, 'W': 20, 'G': 28, 'A': 31, 'C': 20, 'Cj': 28},
    'H': {'F': 12, 'M': 10, 'A': 22},
    'M': {'F': 15, 'H': 10, 'T': 9, 'W': 12, 'Sg': 20},
    'T': {'F': 18, 'M': 9, 'I': 26},
    'J': {'F': 22, 'S': 18, 'TQ': 16},
    'B': {'F': 25},
    'W': {'F': 20, 'M': 12, 'SFe': 22},
    'G': {'F': 28},
    'A': {'F': 31, 'H': 22},
    'C': {'F': 20},
    'Cj': {'F': 28, 'AM': 24, 'SA': 32},
    'S': {'J': 18},
    'TQ': {'J': 16},
    'I': {'T': 26},
    'Sg': {'M': 20},
    'SFe': {'W': 22},
    'AM': {'Cj': 24},
    'SA': {'Cj': 32},
}

# BFS 
def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# DFS 
def dfs(graph, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return path
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None

# Dijkstra 
def dijkstra(graph, start, end):
    heap = [(0, start, [start])]
    visited = set()
    while heap:
        cost, node, path = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        if node == end:
            return path, cost
        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(heap, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')

# Medir tempos com 100 execucoes
N = 100

# BFS
bfs_times = []
for _ in range(N):
    t0 = time.perf_counter()
    path_bfs = bfs(graph, 'S', 'SA')
    tf = time.perf_counter()
    bfs_times.append(tf - t0)
avg_bfs = (sum(bfs_times) / N) * 1000  # em ms

# DFS
dfs_times = []
for _ in range(N):
    t0 = time.perf_counter()
    path_dfs = dfs(graph, 'S', 'SA')
    tf = time.perf_counter()
    dfs_times.append(tf - t0)
avg_dfs = (sum(dfs_times) / N) * 1000

# Dijkstra
dij_times = []
for _ in range(N):
    t0 = time.perf_counter()
    path_dij, cost_dij = dijkstra(graph, 'S', 'SA')
    tf = time.perf_counter()
    dij_times.append(tf - t0)
avg_dij = (sum(dij_times) / N) * 1000

print("=== RESULTADOS ===")
print(f"BFS  - Caminho: {' -> '.join(path_bfs)}")
print(f"BFS  - Tempo médio (100 exec): {avg_bfs:.6f} ms")
print()
print(f"DFS  - Caminho: {' -> '.join(path_dfs)}")
print(f"DFS  - Tempo médio (100 exec): {avg_dfs:.6f} ms")
print()
print(f"Dijkstra - Caminho: {' -> '.join(path_dij)}, Custo total: {cost_dij} km")
print(f"Dijkstra - Tempo médio (100 exec): {avg_dij:.6f} ms")
