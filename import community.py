import community # --> http://perso.crans.org/aynaud/communities/
import networkx as nx
import __init__
import matplotlib.pyplot as plt
newKey = []
nG = nx.Graph()
val_Array = []
Array_Cluster = []
Array = []
ArrayNum = []
with open('C:\\BlackLives.csv', 'r+') as inf:
	next(inf, '')   # skip a line
	G = nx.read_edgelist(inf, delimiter=',', nodetype=str, encoding="utf-8")	
partition = __init__.best_partition(G)
values = [partition.get(node) for node in G.nodes()]
Sort = sorted(partition.values())[len(partition) - 1]
for i in range(0, Sort): #Change Sort Value to fraction if you want to parallelize the code and make it run quicker. See README. 
	CommunityDict = partition.items()
	for key, value in CommunityDict:

		val_Array.append(value)
		if value == i:
			newKey.append(key)
	for tuples in G.edges():
		if tuples[0] in newKey:
			if tuples[1] in newKey:
				nG.add_edge(*tuples)
				G.remove_edge(*tuples)
	Array_Cluster.append(nx.average_clustering(nG))
	ArrayNum.append(nx.number_of_nodes(nG))
	nG.clear()
f = open('C:\\Random.txt', 'w+')
for item in Array_Cluster:
	f.write("%s\n" %item)
f.close()
f = open('C:\\Random.txt', 'r+')
for lines in f.readlines():
	Array.append(float(lines))
plt.plot(ArrayNum, Array, 'ro')
plt.show()
f.close()
f1 = open('C:\\Random1.txt', 'w+')
for item in ArrayNum:
	f1.write("%s\n" %item)