"""
Chapter 7: Tree
This is to compare Depth first search and Breadth First search
The 2 search function will perform search on a file directory system, each algorithms will output a different order
"""

from os import listdir
from os.path import isfile, join


def depth_first_search_printname(
    dir: str, result: list[str] | None = None
) -> list[str]:
    if result is None:
        result = []
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            result.append(file)
        else:
            _ = depth_first_search_printname(fullpath, result)

    return result
