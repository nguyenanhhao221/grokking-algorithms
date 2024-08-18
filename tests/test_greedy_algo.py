from src.greedy_algo import greedy_algo


def test_greedy_algo():
    result = greedy_algo()
    assert result == set(["ktwo", "kthree", "kone", "kfive"])
