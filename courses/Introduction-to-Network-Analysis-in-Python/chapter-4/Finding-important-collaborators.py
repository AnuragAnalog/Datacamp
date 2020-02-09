# Compute the degree centralities of G: deg_cent
deg_cent = nx.degree_centrality(G)

# Compute the maximum degree centrality: max_dc
max_dc = max(list(deg_cent.values()))

# Find the user(s) that have collaborated the most: prolific_collaborators
prolific_collaborators = [n for n in deg_cent.keys() if deg_cent[n] == max_dc]

# Print the most prolific collaborator(s)
print(prolific_collaborators)
