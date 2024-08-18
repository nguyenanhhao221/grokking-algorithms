import pytest

from src.dijkstra_algo import dijkstra_algo


def test_dijkstra_algo(capsys: pytest.CaptureFixture[str]):
    lowest_cost = dijkstra_algo()
    assert lowest_cost == 6

    captured = capsys.readouterr()
    jkwqehqjkweh
    assert "start -> b -> a -> fin" in captured.out
