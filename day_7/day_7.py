from typing import Optional

# Read input data
with open("day_7/input.txt", "r") as f:
    # with open("day_7/input_example.txt", "r") as f:
    input = f.read().strip().splitlines()

input = [line.split() for line in input]


class File:

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Node:

    parent: Optional["Node"]
    dirname: str
    files: dict[str, File]
    children: dict[str, "Node"]
    size: Optional[int]

    def __init__(self, parent: Optional["Node"], dirname: str) -> None:
        self.parent = parent
        self.dirname = dirname
        self.files = {}
        self.children = {}

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Node):
            if (not self.parent) & (not __o.parent):
                return self.dirname == __o.dirname
            elif self.parent and __o.parent:
                return (self.parent == __o.parent) and (self.dirname == __o.dirname)
            else:
                return False
        else:
            return False

    def __repr__(self) -> str:
        return f"{self.dirname}: {self.size}"

    def __hash__(self) -> int:
        if self.parent:
            return self.parent.__hash__() * self.dirname.__hash__()
        else:
            return self.dirname.__hash__()


class FileSystem:

    root_dir: Node
    working_directory: Node
    directories: set[Node]

    def __init__(self) -> None:
        self.root_dir = Node(parent=None, dirname="root")
        self.working_directory = self.root_dir
        self.directories = set()
        self.directories.add(self.root_dir)

    def read_command(self, command: list[str]) -> None:
        if command[0] == '$':
            if command[1] == 'cd':
                if command[2] == '..' and self.working_directory.parent:
                    self.working_directory = self.working_directory.parent
                elif command[2] == '/':
                    self.working_directory = self.root_dir
                else:
                    self.working_directory = self.working_directory.children.get(
                        command[2], self.working_directory)
            elif command[1] == 'ls':
                pass
        else:
            if command[0] == "dir":
                dir_node = Node(self.working_directory, command[1])
                self.working_directory.children[command[1]] = dir_node
                self.directories.add(dir_node)
            else:
                self.working_directory.files[command[1]] = File(
                    command[1], int(command[0]))

    def get_dir_sizes(self, dir: Node) -> None:
        if not dir.children:
            dir.size = sum([file.size for file in dir.files.values()])
        else:
            [self.get_dir_sizes(dir) for dir in dir.children.values()]
            dir.size = sum([file.size for file in dir.files.values(
            )]) + sum([dir.size for dir in dir.children.values() if dir.size])


fs = FileSystem()
[fs.read_command(command) for command in input]
fs.get_dir_sizes(fs.root_dir)

# Part 1
print(
    f"Part 1: answer is: {sum([dir.size for dir in fs.directories if (dir.size and dir.size <= 100000)])}")

# Part 2
needed_space: int = 30000000 - 70000000 + \
    fs.root_dir.size if fs.root_dir.size else 0
print(
    f"Part 2: answer is: {min([dir.size for dir in fs.directories if (dir.size and dir.size >= needed_space)])}")
