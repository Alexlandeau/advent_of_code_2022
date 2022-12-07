# Read input data
with open("day_1/input.txt", "r") as f:
    inventories = [raw_inventory.split("\n") for raw_inventory in f.read().split("\n\n")]
inventories = [[int(item) for item in inventory] for inventory in inventories]

inventories_totals = [sum(inventory) for inventory in inventories]
max_calories = max(inventories_totals)
top_3_calories = sum(sorted(inventories_totals, reverse=True)[:3])


print(f"Part 1: answer is: {max_calories}")
print(f"Part 2: answer is: {top_3_calories}")