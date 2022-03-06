import pathlib
import sys
import itertools


def parse(puzzle_input):
    """Parse input"""
    return [int(op_code) for op_code in puzzle_input.split(',')]


def part1(data):
    """Solve part 1"""
    return execute(data, 12, 2)


def part2(data):
    """Solve part 2"""
    for noun, verb in itertools.product(range(100), repeat=2):
        data_copy = data.copy()
        if execute(data_copy, noun, verb) == 19690720:
            return 100 * noun + verb


def execute(memory, input1, input2):
    memory[1], memory[2] = input1, input2  # Insert input pair at start of memory
    pointer = 0
    while True:
        try:
            if memory[pointer] == 1:  # Addition
                memory[memory[pointer + 3]] = memory[memory[pointer + 1]] + memory[memory[pointer + 2]]
            elif memory[pointer] == 2:  # Multiplication
                memory[memory[pointer + 3]] = memory[memory[pointer + 1]] * memory[memory[pointer + 2]]
            elif memory[pointer] == 99:  # Terminate
                break
            pointer += 4
        except IndexError:
            break
    return memory[0]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)  # Because data is manipulated, parse again
    solution2 = part2(data)
    return solution1, solution2


def main():
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))


if __name__ == "__main__":
    main()
