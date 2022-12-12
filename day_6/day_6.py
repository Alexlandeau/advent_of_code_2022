from collections import deque

# Read input data
with open("day_6/input.txt", "r") as f:
    # with open("day_6/input_example.txt", "r") as f:
    input = f.read()


def find_start(stream: str, maker_length: int) -> int:
    head = deque(stream[:maker_length])
    if len(set(head)) == maker_length:
        return maker_length
    for i, character in enumerate(stream[maker_length:]):
        head.popleft()
        head.append(character)
        if len(set(head)) == maker_length:
            return i + maker_length + 1
    return -1


# Part 1
print(f"Part 1: answer is: {find_start(input, 4)}")

# Part @
print(f"Part 2: answer is: {find_start(input, 14)}")
