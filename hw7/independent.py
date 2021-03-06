from random import randrange
from copy import deepcopy
import sys
from pylab import *
import math

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

def del_neighbors(v, graph):
	result = deepcopy(graph)
	for e in result[v]:
		result.pop(e, None)
	result.pop(v, None)
	return result

def independent2(graph):
	n = len(graph)
	if n <= 1:
		return n
	for v, edges in graph.items():
		in_graph = del_neighbors(v, graph)
		in_count = independent2(in_graph) + 1

		out_graph = deepcopy(graph)
		out_graph.pop(v)
		out_count = independent2(out_graph)
		break
	return max(in_count, out_count)

if __name__ == "__main__":
    ns = []
    result = []
    result2 = []
    for p in range(int(sys.argv[1])):
        n = 2**p
        ns += [n]
        trials = int(sys.argv[2])
        total = 0
        totalSqr = 0
        total2 = 0
        totalSqr2 = 0
        for i in range(trials):
            graph = fill_graph(n)
	    indie = len(independent(graph))
	    indie2 = independent2(graph)
            total += indie
            totalSqr += indie * indie
            total2 += indie2
            totalSqr2 += indie2 * indie2
        result += [(total/trials)]
	result2 += [(total2/trials)]
        Variance = totalSqr/trials - (total/trials)*(total/trials)
        StdDev = sqrt(Variance)
	Variance2 = totalSqr2/trials - (total2/trials)*(total2/trials)
        StdDev2 = sqrt(Variance2)
        print ("n = " + str(n) + "\t gI = " + str(total/trials) + "\t mI = "+ str(total2/trials))
        print ("Variance = " + str(Variance) + "\t stdDev = " + str(StdDev))
	print ("VarianceM = " + str(Variance2) + "\t stdDevM = " + str(StdDev2))
    plot (ns, result, 'o-', ns, result2)
    show()
    subplot(111, xscale = "log", yscale = "log")
    plot (ns, result, 'o-', ns, result2)
    show()
