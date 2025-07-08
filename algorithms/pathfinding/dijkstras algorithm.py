from heapq import heapify, heappop, heappush

graph: dict[str, dict[str, int | float]] = {
    "A": {"B": 3, "C": 3},
    "B": {"A": 3, "D": 3.5, "E": 2.8},
    "C": {"A": 3, "E": 2.8, "F": 3.5},
    "D": {"B": 3.5, "E": 3.1, "G": 10, "M": 4},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"G": 2.5, "C": 3.5},
    "G": {"F": 2.5, "E": 7, "D": 10},
    "M": {"D": 4},
}


class DijkstrasAlgorithm:
    def __init__(self, graph_: dict[str, dict[str, int | float]] = {}):
        self.graph = graph_
        self.distances: dict[str, float | int] = {}

    def shortest_path(self, from_: str, to: str):
        self.distances = {i: float("inf") for i in self.graph}
        self.distances[from_] = 0
        priority_queue: list[tuple[int | float, str]] = [(0, from_)]
        heapify(priority_queue)
        visited: set = set()

        while priority_queue:
            current_distance, current_node = heappop(priority_queue)
            if current_node in visited:
                continue
            visited.add(current_node)

            for neighbour, weight in self.graph[current_node].items():
                tentitive_distcane: float | int = weight + current_distance
                if tentitive_distcane < self.distances[neighbour]:
                    self.distances[neighbour] = tentitive_distcane
                    heappush(priority_queue, (tentitive_distcane, neighbour))

        shortest_path: list[str] = [to]
        current: str = to

        while current != from_:
            for neighbor, weight in self.graph[current].items():
                if self.distances[current] == weight + self.distances[neighbor]:
                    shortest_path.insert(0, neighbor)
                    current = neighbor
        lenght: str = f"length: {self.distances[to]}"
        return shortest_path, lenght


graph_test = DijkstrasAlgorithm(graph_=graph)

result = graph_test.shortest_path(from_="C", to="D")
print(result)
