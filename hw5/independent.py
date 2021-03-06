from random import randrange
import sys

def fill_graph(n):
	graph = {}
	edges = []
	for i in range(n):
		for j in range(n):
			if i == j: continue
			if randrange(0, 2) == 1:	# 1/2 probability
				edges.append((i, j))

	for (u, v) in edges:
		graph[u] = graph.get(u, []) + [v]
		graph[v] = graph.get(v, []) + [u]
	
	for i in range(n):
		graph[i] = set(graph.get(i, []))

	return graph

def independent(graph):
	result = []
	degrees = []
	for v in graph:
		degrees.append((v, len(graph[v])))
	degrees.sort(key=lambda d: d[1])
	
	while(degrees):
		(v, d) = degrees.pop(0)
		result.append(v)
		for u in graph[v]:
			try:
				for (w, deg) in degrees:
					if (u == w): degrees.remove((w, deg))
			except:
				pass
	return result
	print result

if __name__ == "__main__":
	n = int(sys.argv[1])
	trials = int(sys.argv[2])
	graph = fill_graph(n)

	total = 0
	for i in range(trials):
		total += len(independent(graph))
	print("total " + str(total))
	print("average " + str(total / trials))
