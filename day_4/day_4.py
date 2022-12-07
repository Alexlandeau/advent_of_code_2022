# Read input data
with open("day_4/input.txt", "r") as f:
    # with open("day_4/input_example.txt", "r") as f:
    pairs = f.read().splitlines()


def parse_pair(pair):
    parsed_pair = pair.split(",")
    parsed_pair = [pair.split("-") for pair in parsed_pair]
    parsed_pair = [[int(i) for i in assignment] for assignment in parsed_pair]
    return parsed_pair


pairs = [parse_pair(pair) for pair in pairs]


def is_inclusion(pair_1, pair_2):
    return (pair_1[0] <= pair_2[0] and pair_1[1] >= pair_2[1]) or (pair_1[0] >= pair_2[0] and pair_1[1] <= pair_2[1])


def is_overlap(pair_1, pair_2):
    return not (pair_1[1] < pair_2[0] or pair_1[0] > pair_2[1])


# Part 1
nr_inclusions = sum([is_inclusion(pair[0], pair[1]) for pair in pairs])
print(f"Part 1: answer is: {nr_inclusions}")

# Part 2
nr_overlaps = sum([is_overlap(pair[0], pair[1]) for pair in pairs])
print(f"Part 2: answer is: {nr_overlaps}")
