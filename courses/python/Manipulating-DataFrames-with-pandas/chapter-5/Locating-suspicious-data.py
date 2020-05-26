# Create the Boolean Series: sus
sus = ((medals.Event_gender == 'W') & (medals.Gender == 'Men'))

# Create a DataFrame with the suspicious row: suspect
suspect = medals[sus]

# Print suspect
print(suspect)
