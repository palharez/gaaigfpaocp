from collections import deque


def bfs(graph):
    queue = deque()
    queue += graph["you"]
    searched = []
    while queue:
        person = queue.popleft()
        if person in searched:
            continue
        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            print(person + " is not a mango seller!")
            queue += graph[person]
            searched.append(person)


def person_is_seller(person):
    return person[-1] == "m"


if __name__ == "__main__":
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "jonny"]
    graph["anuj"] = []
    graph["peggy"] = []
    graph["thom"] = []
    graph["jonny"] = []
    bfs(graph)
