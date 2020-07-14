# Subset of emails with big numbers: email50_big
email50_big <- email50 %>%
  filter(number == "big")

# Table of the number variable
table(email50_big$number)

# Drop levels
email50_big$number_dropped <- droplevels(email50_big$number)

# Table of the number_dropped variable
table(email50_big$number_dropped)
