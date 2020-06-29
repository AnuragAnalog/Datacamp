# Create speed_vector
speed_vector <- c("medium", "slow", "slow", "medium", "fast")

# Convert speed_vector to ordered factor vector
factor_speed_vector <- factor(speed_vector, order=TRUE, levels=c('slow', 'medium', 'fast'))

# Print factor_speed_vector
factor_speed_vector
summary(factor_speed_vector)
