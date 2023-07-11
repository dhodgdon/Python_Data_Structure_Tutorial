foods1 = {"flour", "pasta", "batter", "pancakes"}
foods2 = {"egg", "pasta", "omelette", "pancakes"}
foods3 = {"milk", "batter", "omelette", "pancakes"}

print("Ingredients:", (foods1 | foods2 | foods3) - (foods1 & foods2) - (foods1 & foods3) - (foods2 & foods3))
print("Gluten-free:", (foods2 | foods3) - foods1)
print("Lactose-free:", (foods1 | foods2) - foods3)
print("Flour/Milk:", foods1 | foods3)
print("Food(s) common to all sets:", foods1 & foods2 & foods3)