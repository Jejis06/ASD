# shortest path between any pair of verticies

# O(n^3)

graph_matrix = list[list[int | float]]
# oo - brak krawedzi

def fl_war(graph:graph_matrix) -> list[list[int | float]]:
    n = len(graph)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] != float('inf') and graph[k][j] != float('inf'):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph






