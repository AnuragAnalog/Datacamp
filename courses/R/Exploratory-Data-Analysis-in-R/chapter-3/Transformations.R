# Create density plot of old variable
gap2007 %>%
  ggplot(aes(x = pop)) +
  geom_density(alpha = 0.3)

# Transform the skewed pop variable
gap2007 <- gap2007 %>%
  mutate(log_pop = log(pop))

# Create density plot of new variable
gap2007 %>%
  ggplot(aes(x = log_pop)) +
  geom_density(alpha = 0.3)
