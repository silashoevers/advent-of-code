from day_base import Day
import parse


class Folder:
    def __init__(self, dirname, parent):
        self.dirname = dirname
        self.children = []
        self.parent = parent

    def get_size(self):
        return sum([child.get_size() for child in self.children])


class File:
    def __init__(self, size, filename, parent):
        self.size = size
        self.filename = filename
        self.parent = parent

    def get_size(self):
        return self.size


class Day7(Day):
    def __init__(self):
        super().__init__(2022, 7, "No Space Left On Device", expected_a=95437, expected_b=24933642)

    def parse(self, puzzle_input):
        return puzzle_input.split('\n')[1:]  # First line is always the same

    def part_a(self, parsed_puzzle_input) -> int:
        # Skip parsing and dive straight into tree building
        root = Folder("/", parent=None)
        current_node = root

        all_nodes = [root]

        for output in parsed_puzzle_input:
            # Is output a command?
            if output[0] == '$':
                if output[2:4] == 'ls':
                    pass
                # parse cd command
                else:
                    dirname = parse.parse("$ cd {}", output).fixed[0]
                    if dirname == "..":
                        current_node = current_node.parent
                    else:
                        current_node = list(filter(lambda f: type(f) == Folder and f.dirname == dirname, current_node.children))[0]
            elif output[:3] == "dir":
                dirname = parse.parse("dir {}", output).fixed[0]
                new_folder = Folder(dirname, current_node)
                current_node.children.append(new_folder)
                all_nodes.append(new_folder)
            else:
                size, filename = parse.parse("{} {}", output).fixed
                new_file = File(int(size), filename, current_node)
                current_node.children.append(new_file)
                all_nodes.append(new_file)

        return sum([folder.get_size() for folder in filter(lambda n: type(n) == Folder and n.get_size() <= 100000, all_nodes)])

    def part_b(self, parsed_puzzle_input) -> int:
        # Skip parsing and dive straight into tree building
        root = Folder("/", parent=None)
        current_node = root

        all_nodes = [root]

        for output in parsed_puzzle_input:
            # Is output a command?
            if output[0] == '$':
                if output[2:4] == 'ls':
                    pass
                # parse cd command
                else:
                    dirname = parse.parse("$ cd {}", output).fixed[0]
                    if dirname == "..":
                        current_node = current_node.parent
                    else:
                        current_node = list(filter(lambda f: type(f) == Folder and f.dirname == dirname, current_node.children))[0]
            elif output[:3] == "dir":
                dirname = parse.parse("dir {}", output).fixed[0]
                new_folder = Folder(dirname, current_node)
                current_node.children.append(new_folder)
                all_nodes.append(new_folder)
            else:
                size, filename = parse.parse("{} {}", output).fixed
                new_file = File(int(size), filename, current_node)
                current_node.children.append(new_file)
                all_nodes.append(new_file)

        free_space = 70000000 - root.get_size()
        size_to_be_deleted = 30000000 - free_space
        candidates = sorted(filter(lambda n: type(n) == Folder and n.get_size() > size_to_be_deleted, all_nodes), key=lambda f: f.get_size())

        return candidates[0].get_size()


if __name__ == '__main__':
    Day7().run()
