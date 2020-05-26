# Melt users: skinny
skinny = pd.melt(users, id_vars=['weekday', 'city'])

# Print skinny
print(skinny)
