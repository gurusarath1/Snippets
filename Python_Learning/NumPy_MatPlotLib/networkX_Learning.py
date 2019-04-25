import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()

G.add_nodes_from([1,2,3])
G.add_edge(2,3)

nx.draw(G)
#nx.draw_random(G)

plt.show()