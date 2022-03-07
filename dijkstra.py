"""
If you wonder why this program is so much commented, it is because it's a demo program for a blog entry I did on Charlie's OIB. Link here :
"""
from timeit import default_timer as timer
from datetime import timedelta
import heapq

"""
Now let's rewrite all the data of our graph in a python dictionary using this method :
'ID of the first node':[(Cost of the path to its Neighbor1, ID of Neighbor 1),(Cost of the path to its Neighbor2, ID of Neighbor2)...]
'ID of the second node':[(Cost of the path to its Neighbor1, ID of Neighbor 1),(Cost of the path to its Neighbor2, ID of Neighbor2)...]
The nodes aren't disposed in any special order
.....
"""
graph = {
    "a":[(15,"o"),(10,"p"),(5,"b"),(10,"h")],
    "p":[(10,"a"),(10,"o")],
    "o":[(15,"a"),(10,"p")],
    "b":[(5,"a"),(10,"h"),(15,"c"),(10,"d")],
    "h":[(10,"b"),(10,"a"),(15,"i"),(10,"k")],
    "c":[(15,"b"),(20,"e")],
    "d":[(10,"b"),(5,"e"),(20,"k")],
    "e":[(5,"d"),(15,"f"),(20,"c")],
    "f":[(15,"e"),(10,"g"),(20,"n")],
    "g":[(10,"f"),(20,"z")],
    "i":[(15,"h"),(10,"j")],
    "j":[(10,"i"),(15,"k"),(15,"l")],
    "k":[(10,"h"),(20,"d"),(15,"j"),(15,"m")],
    "l":[(15,"j"),(15,"m")],
    "m":[(15,"l"),(15,"k"),(10,"n")],
    "n":[(10,"m"),(10,"z"),(20,"f")],
    "z":[(20,"g"),(10,"n")]
}


"""This is the main function containing dijkstra algorithm
here the origin = source
the destination = target
and the data provided by the "linear" form of the graph = graph"""
def dijkstra(graph, source, target):

    #initialisation of the Dijkstra algorithm
    distancetotal = {source: 0} #First cost = 0 because it's simply the origin
    queue = [(distancetotal[source], source)] #Initialisation of the stack
    visited = [] #Here I record all the nodes from which we have visited the neighbors in the main loop of the algorithm
    predecessors = {source:source} #Here I record all the predecessors for each paths explored

    while queue: #The program continue while paths remains unexplored
        distance, to_visit = heapq.heappop(queue) #We explore the most promising path with the lowest values (thus we remove it from our stack) distance = the distance we have accumulated at this node we're going to explore
        for neighbour in graph[to_visit]: #we iterate through neighboring nodes
            dist, name = neighbour[0], neighbour[1] #dist = the distance between the neighbour we're exploring in the new node being visited
            if name not in visited: #we check if the neighbour hasn't already been visited

                """
                We then check if we have not already found the minimal distance from the origin to the concerned node.
                If the path has never been found, it is registered.
                If the path has already been found we compare and if our new path is better then it is registered.
                When there is a change in the total_distance to a node the stack is thus updated
                """
                if name in distancetotal:
                    if (distance+dist) < distancetotal[name]:
                        distancetotal[name] = distance + dist
                        heapq.heappush(queue, (distancetotal[name], name))
                        predecessors[name] = predecessors[to_visit] + "->" + name
                else:
                    distancetotal[name] = distance + dist
                    heapq.heappush(queue, (distancetotal[name], name))
                    predecessors[name] = predecessors[to_visit] + "->" + name

                visited.append(to_visit)
    return predecessors[target], distancetotal[target]

start = timer()
print(dijkstra(graph, "a", "z"))
end = timer()
print(timedelta(seconds=end-start))
