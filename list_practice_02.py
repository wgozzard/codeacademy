inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", 
             "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", 
             "twin bed", "sheets", "sheets", "pillow", "pillow"]

#how many items are in this list
inventory_len = len(inventory)

first = inventory[0]
last = inventory[-1]

#Second item in the list up to not including the 6th item
inventory_2_6 = inventory[2:6]

#What are the first 3 items in inventory
first_3 = inventory[:3]

#count how many twin beds in a list
twin_beds = inventory.count("twin bed")

#remove 5th element from the list
removed_item = inventory.pop(4)

#Add new inventory at 11th position in list
inventory.insert(10, "19th Century Bed Frame")

inventory.sort()

#or could do inventory = sorted(inventory)
#sorted() creates a whole new list

print(inventory)
