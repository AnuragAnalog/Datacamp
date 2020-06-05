# split_low has been created for you
split_low

# Transform: use anonymous function inside lapply
names <- lapply(split_low, function(x) { x[1] })

# Transform: use anonymous function inside lapply
years <- lapply(split_low, function(x) { x[2] })
