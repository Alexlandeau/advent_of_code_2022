from collections import deque
import re
from copy import deepcopy

# Read input data
with open("day_5/input.txt", "r") as f:
    # with open("day_5/input_example.txt", "r") as f:
    input = f.read().split("\n\n")

stacks, procedure = input[0], input[1]
procedure = procedure.split("\n")


def parse_stacks(stacks: str):
    stack_floors = stacks.split("\n")
    stack_nr = len(stack_floors[-1].split())
    stack_floors = [[stack_floor[i: i + 3]
                     for i in range(0, len(stack_floor), 4)] for stack_floor in stack_floors[:-1]]
    parsed_stacks = [deque() for _ in range(stack_nr)]
    [[parsed_stacks[i].append(crate) for i, crate in enumerate(floor)]
     for floor in stack_floors[::-1]]
    parsed_stacks = [[element for element in stack if element != '   ']
                     for stack in parsed_stacks]
    return parsed_stacks


def parse_procedure(procedure: list[str]):
    instruction_pattern = r"move (.*) from (.*) to (.*)"
    parsed_instructions = [re.match(instruction_pattern, instruction).groups()
                           for instruction in procedure]
    parsed_procedure = [{"quantity": int(instruction[0]), "start": int(
        instruction[1])-1, "end": int(instruction[2])-1} for instruction in parsed_instructions]
    return parsed_procedure


def follow_procedure_part_1(procedure, stacks):
    returned_stacks = deepcopy(stacks)
    for instruction in procedure:
        for _ in range(instruction.get("quantity")):
            crate = returned_stacks[instruction.get("start")].pop()
            returned_stacks[instruction.get("end")].append(crate)
    return returned_stacks


def follow_procedure_part_2(procedure, stacks):
    returned_stacks = deepcopy(stacks)
    for instruction in procedure:
        removed_crates = []
        for _ in range(instruction.get("quantity")):
            removed_crates.append(
                returned_stacks[instruction.get("start")].pop())
        [returned_stacks[instruction.get("end")].append(
            crate) for crate in removed_crates[::-1]]
    return returned_stacks


parsed_stacks = parse_stacks(stacks)
parsed_procedure = parse_procedure(procedure)

# Part 1
part_1_stacks = follow_procedure_part_1(parsed_procedure, parsed_stacks)
print(parsed_stacks)
print(
    f"Part 1: answer is: {''.join([stack[-1][1] for stack in part_1_stacks])}")

# Part 2
part_2_stacks = follow_procedure_part_2(parsed_procedure, parsed_stacks)
print(part_2_stacks)
print(
    f"Part 2: answer is: {''.join([stack[-1][1] for stack in part_2_stacks])}")
