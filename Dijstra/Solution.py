class Solution:
    def __init__(self, vertices):
        self.graph = None
        self.V = vertices

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])

    def minDistance(self, dist, visited):
        min_value = float("inf")
        min_index = -1
        for v in range(self.V):
            if dist[v] < min_value and visited[v] == False:
                min_value = dist[v]
                min_index = v
        return min_index

    def dijstra(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0
        visited = [False] * self.V

        for i in range(self.V):
            node = self.minDistance(dist, visited)
            visited[node] = True

            for v in range(self.V):
                if self.graph[node][v] > 0 and visited[v] == False and dist[v] > dist[node] + self.graph[node][v]:
                    dist[v] = dist[node] + self.graph[node][v]

        self.printSolution(dist)


if __name__ == "__main__":
    g = Solution(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
    g.dijstra(0)
