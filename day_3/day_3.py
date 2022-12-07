import string

# Read input data
with open("day_3/input.txt", "r") as f:
# with open("day_3/input_example.txt", "r") as f:
    rucksacks = f.read().splitlines()
rucksacks_with_compartments = []

for rucksakck in rucksacks:
    rucksakck_length = len(rucksakck) // 2
    rucksacks_with_compartments.append([rucksakck[:rucksakck_length], rucksakck[rucksakck_length:]])


def find_common_item(compartments):
    if len(compartments) < 2:
        raise Exception
    else:
        for item in compartments[0]:
            if all([item in compartment for compartment in compartments[1:]]):
                return item
        raise Exception("No duplicate item found")


def prioritize_item(item: str):
    is_uppercase = item.isupper()
    return string.ascii_lowercase.index(item.lower()) + 26 * is_uppercase + 1


# Part 1
common_items = [find_common_item(compartments) for compartments in rucksacks_with_compartments]
common_item_priorities = [prioritize_item(item) for item in common_items]

print(f"Part 1: answer is: {sum(common_item_priorities)}")

# Part 2
common_items = [find_common_item(rucksacks[3*i:3*(i+1)]) for i in range(len(rucksacks) // 3)]
common_item_priorities = [prioritize_item(item) for item in common_items]

print(f"Part 2: answer is: {sum(common_item_priorities)}")
