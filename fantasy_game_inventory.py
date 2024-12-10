# Inventory Display Function
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for item, quantity in inventory.items():
        print(f"{quantity} {item}")  # Print each item and its quantity
        item_total += quantity
    print(f"Total number of items: {item_total}")  # Print the total count of items

# Add Loot to Inventory Function
def addToInventory(inventory, addedItems):
    for item in addedItems:  # Loop through each item in the loot list
        if item in inventory:
            inventory[item] += 1  # If item exists, increase its quantity
        else:
            inventory[item] = 1  # If item doesn't exist, add it with quantity 1
    return inventory

# Example Usage
# Initial inventory
inv = {'gold coin': 42, 'rope': 1}

# Loot from a dragon
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Update the inventory with the loot
inv = addToInventory(inv, dragonLoot)

# Display the updated inventory
displayInventory(inv)
