# Read input data
with open("day_8/input.txt", "r") as f:
    # with open("day_8/input_example.txt", "r") as f:
    input = f.read().strip().split()


class Spot():
    height: int
    max_top: int
    max_bottom: int
    max_left: int
    max_right: int
    view_top: int
    view_bottom: int
    view_left: int
    view_right: int
    is_visible: bool
    view_score: int

    def __init__(self, height: int,
                 max_top: int = -1,
                 max_bottom: int = -1,
                 max_left: int = -1,
                 max_right: int = -1,
                 view_top: int = 0,
                 view_bottom: int = 0,
                 view_left: int = 0,
                 view_right: int = 0) -> None:
        self.height = height
        self.max_bottom = max_bottom
        self.max_left = max_left
        self.max_right = max_right
        self.max_top = max_top
        self.view_top = view_top
        self.view_right = view_right
        self.view_left = view_left
        self.view_bottom = view_bottom

    def compute_visibility(self):
        self.is_visible = any([self.height > max_from_direction for max_from_direction in (
            self.max_top, self.max_bottom, self.max_left, self.max_right)])

    def compute_view_score(self):
        self.view_score = self.view_bottom * \
            self.view_left * self.view_right * self.view_top

    def __repr__(self) -> str:
        return self.__dict__.__str__()


def propagate_max_left(grid: list[list[Spot]]) -> None:
    for row in grid:
        for i, spot in enumerate(row[1:]):
            spot.max_left = max(row[i].height, row[i].max_left)


def propagate_max_right(grid: list[list[Spot]]) -> None:
    for row in grid:
        for i, spot in enumerate(reversed(row[:-1])):
            spot.max_right = max(
                row[len(row)-i-1].height, row[len(row)-i-1].max_right)


def propagate_max_top(grid: list[list[Spot]]) -> None:
    for i, row in enumerate(grid[1:]):
        for j, spot in enumerate(row):
            spot.max_top = max(grid[i][j].height, grid[i][j].max_top)


def propagate_max_bottom(grid: list[list[Spot]]) -> None:
    for i, row in enumerate(reversed(grid[0:-1])):
        for j, spot in enumerate(row):
            spot.max_bottom = max(
                grid[len(grid)-i-1][j].height, grid[len(grid)-i-1][j].max_bottom)


def compute_visibility_in_row(spot_index: int, row: list[Spot]) -> tuple[int, int]:
    target_spot = row[spot_index]
    view_left = 0
    view_right = 0
    if spot_index == 0:
        view_left = 0
    else:
        for spot in reversed(row[:spot_index]):
            view_left += 1
            if target_spot.height > spot.height:
                continue
            else:
                break
    if spot_index == len(row)-1:
        view_right = 0
    else:
        for spot in row[spot_index + 1:]:
            view_right += 1
            if target_spot.height > spot.height:
                continue
            else:
                break
    return (view_left, view_right)


def compute_visibilities(grid: list[list[Spot]]) -> None:
    for row in grid:
        for i in range(len(row)):
            row[i].view_left, row[i].view_right = compute_visibility_in_row(
                i, row)
    for col in zip(*grid):
        for i in range(len(col)):
            col[i].view_top, col[i].view_bottom = compute_visibility_in_row(
                i, list(col))


def find_visible_trees(grid: list[list[Spot]]) -> None:
    propagate_max_top(grid)
    propagate_max_bottom(grid)
    propagate_max_left(grid)
    propagate_max_right(grid)
    compute_visibilities(grid)
    for row in grid:
        for spot in row:
            spot.compute_visibility()
            spot.compute_view_score()


grid: list[list[Spot]] = [[Spot(int(height))
                           for height in row] for row in input]
find_visible_trees(grid)

# Part 1
print(
    f"Part 1: answer is: {sum([sum([spot.is_visible for spot in row]) for row in grid])}")

# Part 2
print(
    f"Part 2: answer is: {max([max([spot.view_score for spot in row]) for row in grid])}")
