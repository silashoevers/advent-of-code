from collections import deque
from day_base import Day
import parse

# Quick hack as we can peek at the size of the example and input beforehand
# width, height = 3, 3  # Example size
width, height = 9, 8  # Input size


class Day5(Day):
    def __init__(self):
        super().__init__(2022, 5, "Supply Stacks", expected_a='CMZ', expected_b='MCD')

    def parse(self, puzzle_input):
        """
        Encode starting state into list of deques and instructions into tuples of (amount_moved, start_stack, end_stack)
        """
        starting_state, move_instructions = puzzle_input.split('\n\n')

        # Encode starting state
        temp_stacks = []
        for _ in range(width):
            temp_stacks.append([])
        for layer in starting_state.split('\n')[:-1]:
            splitted_layer = [layer[i:i+4] for i in range(0, len(layer), 4)]
            for stack_number, spot in enumerate(splitted_layer):
                potential_crate = parse.search("[{}]", spot)
                if potential_crate is not None:
                    temp_stacks[stack_number].append(potential_crate.fixed[0])

        # Replace lists with deques and reorder
        stacks = []
        for temp_stack in temp_stacks:
            stacks.append(deque(reversed(temp_stack)))

        # Parse move instructions
        parsed_instructions = []
        for move_instruction in move_instructions.split('\n'):
            parse_format = "move {} from {} to {}"
            amount_moved, start_stack, end_stack = parse.parse(parse_format, move_instruction).fixed
            parsed_instructions.append(map(int, (amount_moved, start_stack, end_stack)))

        return stacks, parsed_instructions

    def part_a(self, parsed_puzzle_input):
        stacks, move_instructions = parsed_puzzle_input
        for amount_moved, start_stack, end_stack in move_instructions:
            for _ in range(amount_moved):
                picked_up_crate = stacks[start_stack-1].pop()    # Crane picks up crate
                stacks[end_stack-1].append(picked_up_crate)      # Crane puts back crate
        result = []
        for stack in stacks:
            # TODO: Account for potential edge case of empty stack?
            result.append(stack.pop())
        return ''.join(result)

    def part_b(self, parsed_puzzle_input):
        stacks, move_instructions = parsed_puzzle_input
        for amount_moved, start_stack, end_stack in move_instructions:
            picked_up_crates = []
            for _ in range(amount_moved):
                picked_up_crates.append(stacks[start_stack-1].pop())
            stacks[end_stack-1].extend(reversed(picked_up_crates))
        result = []
        for stack in stacks:
            result.append(stack.pop())
        return ''.join(result)


if __name__ == '__main__':
    Day5().run()
