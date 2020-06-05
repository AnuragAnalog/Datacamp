# Pre-defined variables
rquote <- "r's internals are irrefutably intriguing"
chars <- strsplit(rquote, split = "")[[1]]

# Initialize rcount
rcount <- 0

# Finish the for loop
for (char in chars) {
  if (char == 'r')
  {
    rcount = rcount + 1
  }
  else if (char == 'u')
  {
    break
  }
  
}

# Print out rcount
print(rcount)
