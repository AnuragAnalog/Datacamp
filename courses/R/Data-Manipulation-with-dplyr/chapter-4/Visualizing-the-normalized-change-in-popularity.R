# Filter for the names Steven, Thomas, and Matthew
names_filtered <- names_normalized %>%
  filter(name %in% c('Steven', 'Thomas', 'Matthew'))

# Visualize these names over time
  ggplot(names_filtered, aes(x=year, y=fraction_max, color=name)) + geom_line()
