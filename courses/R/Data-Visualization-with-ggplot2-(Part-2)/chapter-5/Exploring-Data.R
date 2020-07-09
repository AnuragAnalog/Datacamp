# Explore the dataset with summary and str
summary(adult)
str(adult)

# Age histogram
ggplot(adult, aes(SRAGE_P)) +
  geom_histogram()

# BMI value histogram
ggplot(adult, aes(BMI_P)) +
  geom_histogram()

# Age colored by BMI, binwidth = 1
ggplot(adult, aes(SRAGE_P, fill = factor(RBMI))) +
  geom_histogram(binwidth = 1)
