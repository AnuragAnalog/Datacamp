# Compute the degree of every node: degrees
degrees = [len(list(T.neighbors(node))) for node in T.nodes()]

# Print the degrees
print(degrees)
