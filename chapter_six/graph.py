from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
      

# person_is_seller is a dummy function 
def person_is_seller(person): 
    return True if person == 'jonny' else False

def bfs(graph):
    search_queue  = deque()
    search_queue.append( "you")
    search_queue.extend(graph["you"] ) ## extend at the end of the queue

    while search_queue: 
        person = search_queue.popleft() ## deletes and returns first element added        
        if person_is_seller(person): 
            print('person ', person, " is a seller")
            return True
        else : 
            search_queue.extend(graph.get(person))

bfs(graph)