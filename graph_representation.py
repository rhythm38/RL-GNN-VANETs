import networkx as nx
import numpy as np

def create_graph(data, communication_range):
    G = nx.Graph()
    for i, vehicle in enumerate(data):
        G.add_node(i, features=vehicle['features'])
    
    for i, vi in enumerate(data):
        for j, vj in enumerate(data):
            if i != j:
                dist = np.linalg.norm(np.array(vi['position']) - np.array(vj['position']))
                if dist <= communication_range:
                    similarity = np.dot(vi['direction'], vj['direction']) + 1 / (1 + dist)
                    G.add_edge(i, j, weight=similarity)
    return G
