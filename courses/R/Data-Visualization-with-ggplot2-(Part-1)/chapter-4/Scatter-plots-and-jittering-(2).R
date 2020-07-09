# Examine the structure of Vocab
str(Vocab)

# Basic scatter plot of vocabulary (y) against education (x). Use geom_point()
ggplot(Vocab, aes(education, vocabulary)) + geom_point()

# Use geom_jitter() instead of geom_point()
ggplot(Vocab, aes(education, vocabulary)) + geom_jitter()

# Using the above plotting command, set alpha to a very low 0.2
ggplot(Vocab, aes(education, vocabulary)) + geom_jitter(alpha = 0.2)

# Using the above plotting command, set the shape to 1
ggplot(Vocab, aes(education, vocabulary)) + geom_jitter(alpha = 0.2, shape = 1)
