from heapq import heapify, heappop, heappush

graph: dict[str, dict[str, int | float]] = {
    "A": {"B": 3, "C": 3, "H": 4.2},
    "B": {"A": 3, "D": 3.5, "E": 2.8, "I": 2.9},
    "C": {"A": 3, "E": 2.8, "F": 3.5, "J": 3.3},
    "D": {"B": 3.5, "E": 3.1, "G": 10, "M": 4.7},
    "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
    "F": {"C": 3.5, "G": 2.5, "K": 1.8},
    "G": {"F": 2.5, "E": 7, "D": 10, "L": 5.1},
    "H": {"A": 4.2},
    "I": {"B": 2.9},
    "J": {"C": 3.3},
    "K": {"F": 1.8},
    "L": {"G": 5.1},
    "M": {"D": 4.7},
}


class DijkstrasAlgorithm:
    def __init__(self, graph_: dict[str, dict[str, int | float]] = {}):
        self.graph = graph_
        self.distances: dict[str, float | int] = {}

    def shortest_path(self, from_: str, to: str ):
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
                    heappush(priority_queue,(tentitive_distcane, neighbour))
                    
    
        shortest_path:list[str] = [to]
        current:str = to

        while current!= from_:
            found: bool = False
            for short in self.distances:
                if found is True:
                    break
                for neighbor, weight in self.graph[current].items():
                    if self.distances[current] == weight +  self.distances[short]:
                        shortest_path.append(neighbor)
                        current = neighbor
                        found = True
        return shortest_path
            
    # def shortest_path(self, source: str, target: str):
    #     _, predecessors = self.distances.items()
    #     path: list[str] = []
    #     current_node = target
        
    #     while current_node:
    #         path.append(current_node)
    #         current_node = predecessors[current_node]

    #     # Reverse the path and return it
    #     path.reverse()

    #     return path
        

graph_test = DijkstrasAlgorithm(graph_=graph)

result = graph_test.shortest_path(from_="M", to="J")
print(result)
