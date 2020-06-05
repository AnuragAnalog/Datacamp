# Finish the pow_two() function
pow_two <- function(x, print_info = TRUE) {
  y <- x ^ 2
  if (print_info == TRUE)
  {
    print(paste(x, "to the power two equals", y))
  }
  return(y)
}
