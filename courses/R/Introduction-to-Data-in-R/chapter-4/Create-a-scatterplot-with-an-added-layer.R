# Scatterplot of score vs. bty_avg colored by cls_type
ggplot(evals, aes(bty_avg, score, color=cls_type)) +
  geom_point()
