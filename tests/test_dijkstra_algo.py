from src.dijkstra_algo import dijkstra_algo


def test_dijkstra_algo():
    lowest_cost = dijkstra_algo()
    assert lowest_cost == 6
