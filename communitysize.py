import collections
import matplotlib.pyplot as plt
import networkx as nx
import math
import __init__
countArray = []
numberArray = []
with open('C:\\Berlin.csv', 'r+') as inf:
	next(inf, '')   # skip a line
	G = nx.read_edgelist(inf, delimiter=',', nodetype=str, encoding="utf-8")
partition = __init__.best_partition(G)
values = [partition.get(node) for node in G.nodes()]
print partition
Sort = sorted(partition.values())[len(partition) - 1]
print Sort
for i in range(0, Sort):
	var = 0
	Random = partition.items()
	for key, value in Random:
		if value == i:
			var = var +1
			G.remove_node(key)
	countArray.append(var)
	numberArray.append(i)
	print i
print countArray
plt.plot(numberArray, countArray, 'ro')

plt.show()