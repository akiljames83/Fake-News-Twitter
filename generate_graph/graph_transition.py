from igraph import *
from Pypeline.Pypes.Queue import Queue

# Global variables for mapping of graph nodes
count = 0
node_map = dict()
node_arr = list()
node_connections = dict()
connections = set()

graph = Graph()

# File -> The graph initial state with connections
file1 = 'graph_rep.txt'
# File2 -> The newly affected nodes after each iteration
fileT = 'graph_transitions.txt'
# Graph data generated
fileD = 'graph_data.txt'

# Open textfile and reduce array of values to 0 based index values
with open(fileD, 'r') as f:
	for line in f:
		for pair in line.split(";"):
			if not pair: continue
			node_l = int(pair.split(",")[0])
			node_r = int(pair.split(",")[1])
			
			if node_l not in node_map:
				node_map[node_l] = count
				node_arr.append(node_l)
				count += 1

			if node_r not in node_map:
				node_map[node_r] = count
				node_arr.append(node_r)
				count += 1

			# Undirected graph representation ensured with this portion 
			new_connect = "{}-{}".format(
				min(node_map[node_l],node_map[node_r]),
				max(node_map[node_l],node_map[node_r])
			)

			if node_l not in node_connections:
				node_connections[node_l] = set([node_r])
			else:
				node_connections[node_l].add(node_r)

			if node_r not in node_connections:
				node_connections[node_r] = set([node_l])
			else:
				node_connections[node_r].add(node_l)

			if new_connect in connections:
				continue

			# Add new connection to the set of connections
			connections.add(new_connect)

			# Add more verticies if needed and then create the edge
			graph.add_vertices(count - graph.vcount())
			graph.add_edges([(node_map[node_l],node_map[node_r])])

print("Number of nodes:",count)

# State transitions
seen = set([node_arr[0]])
queue = Queue(maxlen=1e9)
queue.enqueue(node_arr[0])

with open(fileT, 'w') as out:
	out.write("{}\n".format(node_arr[0]))
	while queue.sizeQueue():
		cur = queue.peek()
		transition = ""
		for j,i in enumerate(node_connections[cur]):
			if i not in seen:
				if j + 1 == len(node_connections[cur]):
					transition += "{}".format(i)
				else:
					transition += "{},".format(i)
				queue.enqueue(i)
				seen.add(i)
		if transition:
			out.write(transition + "\n")

		queue.dequeue()
