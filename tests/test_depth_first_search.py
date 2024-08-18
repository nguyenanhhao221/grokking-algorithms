from src.depth_first_search import depth_first_search_printname


def test_depth_first_search() -> None:
    expected: list[str] = ["a.png", "space.png", "odyssey.png"]
    output: list[str] = depth_first_search_printname(dir="tests/pics")
    assert output == expected
