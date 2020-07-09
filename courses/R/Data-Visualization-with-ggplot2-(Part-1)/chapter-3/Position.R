# The base layer, cyl.am, is available for you
# Add geom (position = "stack" by default)
cyl.am + 
  geom_bar()

# Fill - show proportion
cyl.am + 
  geom_bar(position = 'fill')  

# Dodging - principles of similarity and proximity
cyl.am +
  geom_bar(position = 'dodge') 

# Clean up the axes with scale_ functions
val = c("#E41A1C", "#377EB8")
lab = c("Manual", "Automatic")
cyl.am +
  geom_bar(position = "dodge") +
  scale_x_discrete('Cylinders') + 
  scale_y_continuous('Number') +
  scale_fill_manual('Transmission', values = val,labels = lab)
