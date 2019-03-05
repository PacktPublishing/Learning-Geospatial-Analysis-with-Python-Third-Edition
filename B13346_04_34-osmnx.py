import osmnx as ox
G = ox.graph_from_place('Bay Saint Louis, MS , USA', network_type='drive')
stats = ox.basic_stats(G)
stats["street_length_avg"]