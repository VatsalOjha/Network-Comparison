import collections
import matplotlib.pyplot as plt
import networkx as nx
import math
import __init__
newArray = []
with open('C:\\isis.csv', 'r+') as inf:
	next(inf, '')   # skip a line
	G = nx.read_edgelist(inf, delimiter=',', nodetype=str, encoding="utf-8")
dictionary = G.degree()
degree_sequence=sorted([dictionary.values()], reverse=True) # degree sequence
graphdict = collections.Counter(dictionary.values())
print graphdict
for i in graphdict.values():
	if i != 0:
		newArray.append(math.log(i, 10))
	else:
		newArray.append(0)
plt.plot(graphdict.keys(), newArray, 'ro')
plt.show()