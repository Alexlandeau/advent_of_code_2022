from typing import Generator
from enum import Enum

# Read input data
with open("day_9/input.txt", "r") as f:
    # with open("day_9/input_example.txt", "r") as f:
    input = f.read().strip().splitlines()


class Direction(Enum):
    U = 'U'
    D = 'D'
    L = 'L'
    R = 'R'


class Knot():
    x: int
    y: int
    visited_positions: set[tuple[int, int]]

    def __init__(self, starting_position: tuple[int, int]) -> None:
        self.x = starting_position[0]
        self.y = starting_position[1]
        self.visited_positions = {starting_position}

    def get_position(self) -> tuple[int, int]:
        return (self.x, self.y)


class Head(Knot):

    def __init__(self, starting_position: tuple[int, int]) -> None:
        super().__init__(starting_position)

    def move(self, direction: Direction, distance: int) -> Generator[tuple[int, int], None, None]:
        if direction.value == 'U':
            for _ in range(distance):
                self.x += 1
                current_position = self.get_position()
                self.visited_positions.add(current_position)
                yield current_position
        elif direction.value == 'D':
            for _ in range(distance):
                self.x -= 1
                current_position = self.get_position()
                self.visited_positions.add(current_position)
                yield current_position
        elif direction.value == 'L':
            for _ in range(distance):
                self.y -= 1
                current_position = self.get_position()
                self.visited_positions.add(current_position)
                yield current_position
        else:
            for _ in range(distance):
                self.y += 1
                current_position = self.get_position()
                self.visited_positions.add(current_position)
                yield current_position


class Tail(Knot):

    def __init__(self, starting_position: tuple[int, int]) -> None:
        super().__init__(starting_position)

    def get_vector_to_knot(self, knot: Knot) -> tuple[int, int]:
        return (knot.x-self.x, knot.y-self.y)

    def is_touching_knot(self, knot: Knot) -> bool:
        vector_to_knot = self.get_vector_to_knot(knot)
        distance_to_knot = vector_to_knot[0]**2 + vector_to_knot[1]**2
        return distance_to_knot <= 2

    def move(self, move_to_perform: tuple[int, int]) -> None:
        self.x += move_to_perform[0]
        self.y += move_to_perform[1]
        current_position = self.get_position()
        self.visited_positions.add(current_position)

    def follow_knot(self, knot: Knot) -> None:
        if not self.is_touching_knot(knot):
            vector_to_knot = self.get_vector_to_knot(knot)
            move_to_perform: tuple[int, int] = (vector_to_knot[0]//abs(vector_to_knot[0]) if vector_to_knot[0] !=
                                                0 else 0,
                                                vector_to_knot[1]//abs(vector_to_knot[1]) if vector_to_knot[1] !=
                                                0 else 0)
            self.move(move_to_perform)


input = [move.split() for move in input]
moves: list[tuple[Direction, int]] = [
    (Direction[move[0]], int(move[1])) for move in input]


# Part 1

head = Head((0, 0))
tail = Tail((0, 0))
for move in moves:
    for step in head.move(move[0], move[1]):
        tail.follow_knot(head)

print(
    f"Part 1: answer is: {len(tail.visited_positions)}")


# Part 2

head = Head((0, 0))
tails = [Tail((0, 0)) for _ in range(9)]
for move in moves:
    for step in head.move(move[0], move[1]):
        tails[0].follow_knot(head)
        for i in range(1, len(tails)):
            tails[i].follow_knot(tails[i-1])

print(
    f"Part 2: answer is: {len(tails[-1].visited_positions)}")
