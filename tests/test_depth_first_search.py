from src.depth_first_search import depth_first_search_printname


def test_depth_first_search():
    expected = ["a.png", "space.png", "odyssey.png"]
    output = depth_first_search_printname(dir="tests/pics")
    assert output == expected
