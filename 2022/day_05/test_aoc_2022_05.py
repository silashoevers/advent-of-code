import pathlib
import pytest
import aoc_2022_05 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == (
        [['Z', 'N'], ['M', 'C', 'D'], ['P']], [  # Stacks are bottom to top
            (1, 2, 1),  # move 1 from 2 to 1
            (3, 1, 3),
            (2, 2, 1),
            (1, 1, 2),
        ]
    )

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part1(example2) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part2(example1) == ...
