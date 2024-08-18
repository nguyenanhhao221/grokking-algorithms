"""
Implement the Dijkstra algorithms
"""

import math


def dijkstra_algo():
    # we initialized the graph
    graph: dict[str, dict[str, int | float]] = {}
    graph["start"] = {}
    graph["start"]["a"] = 6
    graph["start"]["b"] = 2

    graph["a"] = {}
    graph["a"]["fin"] = 1

    graph["b"] = {}
    graph["b"]["a"] = 3
    graph["b"]["fin"] = 5

    # The fin node dont have any out neighbors
    graph["fin"] = {}

    infinity = math.inf

    # cost hash table to store cost to each node
    costs: dict[str, int | float] = {}
    costs["a"] = 6
    costs["b"] = 2
    costs["fin"] = infinity

    # hash table for parent
    parents: dict[str, str | None] = {}
    parents["a"] = "start"
    parents["b"] = "start"
    parents["fin"] = None

    # keep track of the node that were processed
    processed: set[str] = set()

    lowest_node = find_lowest_cost_node(costs=costs, processed=processed)

    while lowest_node is not None:
        out_neighbors = graph[lowest_node]
        # Calculate the cost to get to all out_neighbors
        for target in out_neighbors.keys():
            cost_to_target = out_neighbors[target] + costs[lowest_node]

            if cost_to_target < costs[target]:
                # Update the costs hash table
                costs[target] = cost_to_target
                # Update the parents hash table
                parents[target] = lowest_node

        processed.add(lowest_node)
        lowest_node = find_lowest_cost_node(costs=costs, processed=processed)

    print(f"Lowest cost to get to fin is : {costs["fin"]}")
    print("Path with lowest cost")
    print_path_with_lowest_cost(parents)
    return costs["fin"]


def find_lowest_cost_node(costs: dict[str, int | float], processed: set[str]):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def print_path_with_lowest_cost(parents: dict[str, str | None]):
    result: list[str] = ["fin"]
    value = parents["fin"]
    while value is not None:
        result.insert(0, value)
        value = parents.get(value)

    print(" -> ".join(result))


if __name__ == "__main__":
    dijkstra_algo()
