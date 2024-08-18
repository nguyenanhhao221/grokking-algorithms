import pytest

from src.breadth_first_search import breadth_first_search


def test_breadth_search(capsys: pytest.CaptureFixture[str]):
    graph: dict[str, list[str]] = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []

    result = breadth_first_search(graph=graph)
    captured = capsys.readouterr()
    # Check the print output
    assert "thom" in captured.out
    assert result
