from min_dalle import MinDalle
model = MinDalle(is_mega=True, is_reusable=True)

text = "robots enjoying sunset in paris" 
seed = 6  
grid_size = 2  

display(model.generate_image(text, seed, grid_size))