# Route along a road network

# http://git.io/vcXFQ

import networkx as nx
import math
from itertools import tee
import shapefile
import os

savedir = "."

def haversine(n0, n1):
    """Calculate the distance between two points"""
    x1, y1 = n0
    x2, y2 = n1
    x_dist = math.radians(x1 - x2)
    y_dist = math.radians(y1 - y2)
    y1_rad = math.radians(y1)
    y2_rad = math.radians(y2)
    a = math.sin(y_dist/2)**2 + math.sin(x_dist/2)**2 \
        * math.cos(y1_rad) * math.cos(y2_rad)
    c = 2 * math.asin(math.sqrt(a))
    distance = c * 6371
    return distance

def pairwise(iterable):
    """Return an iterable in tuples of two
    s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# Shapefile containing our road network
shp = "road_network.shp"

# Create our networkx directional graph
G = nx.DiGraph()

# Use the lines in our road shapefile
# to build a connected graph
r = shapefile.Reader(shp)
for s in r.shapes():
    for p1, p2 in pairwise(s.points):
        G.add_edge(tuple(p1), tuple(p2))

# Extract a connected component subgraph for routing
sg = list(nx.connected_component_subgraphs(G.to_undirected()))[0]

# Read in our starting point and routing destination
r = shapefile.Reader("start_end")
start = r.shape(0).points[0]
end = r.shape(1).points[0]

# Calculate the length of each element of the graph
for n0, n1 in sg.edges_iter():
  dist = haversine(n0, n1)
  sg.edge[n0][n1]["dist"] = dist

nn_start = None
nn_end = None

start_delta = float("inf")
end_delta = float("inf")

# Find the graph nodes closes to the 
# start and destination points
for n in sg.nodes():
    s_dist = haversine(start, n)
    e_dist = haversine(end, n)
    if s_dist < start_delta:
        nn_start = n
        start_delta = s_dist
    if e_dist < end_delta:
        nn_end = n 
        end_delta = e_dist

# Find the shortest route between the start and end nodes
path = nx.shortest_path(sg, source=nn_start, target=nn_end, weight="dist")

# save the route as a shapefile
w = shapefile.Writer(shapefile.POLYLINE)
w.field("NAME", "C", 40)
w.line(parts=[[list(p) for p in path]])
w.record("route")
w.save(os.path.join(savedir, "route"))
