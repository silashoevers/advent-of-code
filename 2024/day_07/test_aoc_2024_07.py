import pathlib
import pytest
import aoc_2024_07 as aoc

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
    assert example1 == [(190, [10, 19]), (3267, [81, 40, 27]), (83, [17, 5]), (156, [15, 6]),
                        (7290, [6, 8, 6, 15]), (161011, [16, 10, 13]), (192, [17, 8, 14]),
                        (21037, [9, 7, 18, 13]), (292, [11, 6, 16, 20])]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 3749

def test_part2_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part2(example1) == 11387

def test_part2_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part2(example2) == 666