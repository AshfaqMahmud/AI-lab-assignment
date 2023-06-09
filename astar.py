import heapq

def Astar(graph, start, goal):
    pq = []                             #Create a priority queue (often implemented as a min-heap) to store nodes to be explored.
    heapq.heappush(pq, (0, start))

    #Initialize dictionaries to store the cost from the start node (g_score) and the total estimated cost to the goal node (f_score) for each node in the graph.
    prev = dict()
    cost = dict()
    prev[start] = None
    cost[start] = 0

    while pq:
        current = heapq.heappop(pq)[1]
        
        if current == goal:
            break

        for adjacent in graph[current]:

            new_cost = cost[current] + graph[current][adjacent]
#           print(current)
#           print(adjacent)
#           print(graph[current][adjacent])
#           print(cost[current])
#           print(new_cost)
            if adjacent not in cost or new_cost < cost[adjacent]:
                cost[adjacent] = new_cost
                priority = new_cost + hsld[adjacent]
                heapq.heappush(pq, (priority, adjacent))
                prev[adjacent] = current
            #print(priority)
    return prev, cost

def track_path(prev, start, goal):
    path = [goal]
    node = goal
    while node != start:
        node = prev[node]
        path.append(node)
    path.reverse()
    return path

graph = {'Oradea':{'Zerind':71,'Sibiu':151},'Zerind':{'Oradea':71,'Arad':75},
          'Arad':{'Zerind':75,'Timisoara':118,'Sibiu':140},
          'Timisoara':{'Arad':118,'Lugoj':111},
          'Lugoj':{'Timisoara':111,'Mehadia':70},
          'Mehadia':{'Lugoj':70,'Dobreta':70},
          'Dobreta':{'Mehadia':75,'Craiova':120},
          'Craiova':{'Dobreta':120,'Rimnicu Vilcea':146,'Pitesti':138},
          'Sibiu':{'Arad':140,'Oradea':151,'Rimnicu Vilcea':80,'Fagaras':99},
          'Rimnicu Vilcea':{'Sibiu':80,'Craiova':146,'Pitesti':97},
          'Fagaras':{'Sibiu':99,'Bucharest':221},
          'Pitesti':{'Bucharest':101,'Rimnicu Vilcea':97,'Craiova':138},
          'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},
          'Giurgiu':{'Bucharest':90},
          'Urziceni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},
          'Hirsova':{'Urziceni':98,'Eforie':86},
          'Eforie':{'Hirsova':86},
          'Vaslui':{'Urziceni':142,'Iasi':92},
          'Iasi':{'Neamt':87,'Vaslui':92},
          'Neamt':{'Iasi':87}}
hsld = {'Arad':366, 'Bucharest':0, 'Craiova':160, 'Dobreta':242, 'Eforie':161, 'Fagaras':176, 'Giurgiu':77, 'Hirsova':151, 'Iasi':226, 'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380, 'Pitesti':100, 'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329, 'Urziceni':80, 'Vaslui':199, 'Zerind':374}

start = 'Arad'
goal = 'Bucharest'

prev, cost = Astar(graph, start, goal)
path = track_path(prev, start, goal)

print(f"Path: {path}")
print(f"Cost: {cost[goal]}")