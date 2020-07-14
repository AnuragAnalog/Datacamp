# Load packages
library(dplyr)

# Count number of male and female applicants admitted
ucb_admit %>%
  count(Gender, Admit)
