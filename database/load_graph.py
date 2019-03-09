import random
import time

TIMESTAMP = int(time.time())
connections = dict()

# Total is 14,850,000 ish
def shuffle(file):
	lines = open("reduced-higgs.txt").readlines()
	random.shuffle(lines)
	open(file,'w').writelines(lines)

def init_graph(size, file):
	with open(file, "r") as f:
		# Just do first 20k
		graph = ""
		for i, line in enumerate(f):
			if i == size: break

			a, b = (int(i) for i in line.strip().split(" "))
			if a in connections:
				connections[a].add(b)
			else:
				connections[a] = set([b])
			graph += "{},{};".format(a,b)
	with open("graph_data.txt", "w") as of:
		of.write(graph)
	with open("..\\generate_graph\\graph_data.txt", "w") as of:
		of.write(graph)

def reduce():
	with open("higgs-social_network.edgelist","r") as h:
		with open("reduced-higgs.txt","w") as f:
			for i, line in enumerate(h):
				if i == 2e4: break
				f.write(line)

file = "shuffle_edges.txt"
reduce()
shuffle(file)
init_graph(2e3,file)