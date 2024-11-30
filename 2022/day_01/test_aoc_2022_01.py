import pathlib
import pytest
import aoc_2022_01 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [[1000,2000,3000],[4000],[5000,6000],[7000,8000,9000],[10000]]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 24000

def test_part2_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part2(example1) == 45000
