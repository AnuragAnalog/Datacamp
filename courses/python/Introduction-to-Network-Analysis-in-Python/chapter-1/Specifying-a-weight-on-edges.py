# Set the weight of the edge
T.edges[1, 10]['weight'] = 2

# Iterate over all the edges (with metadata)
for u, v, d in T.edges(data=True):
    # Check if node 293 is involved
    if 293 in [u, v]:
        # Set the weight to 1.1
        T.edges[u, v]['weight'] = 1.1
