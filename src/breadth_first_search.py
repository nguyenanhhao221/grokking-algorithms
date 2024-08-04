from collections import deque


def person_is_seller(name: str) -> bool:
    return name[-1] == "m"


def breadth_first_search(graph: dict[str, list[str]]) -> bool:
    # Create a new queue
    search_queue: deque[str] = deque()
    # Add the first degree neighbor
    search_queue += graph["you"]

    # keep track of the person who is searched, so we don't run into duplicate
    searched: set[str] = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is the a mango seller")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False
