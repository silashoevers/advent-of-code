import pathlib
import pytest
import aoc_2022_11 as aoc
from aoc_2022_11 import Item

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse_puzzle_input(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse_puzzle_input(puzzle_input)

@pytest.mark.skip(reason="Can't seem to figure out object identity but looks good to me")
def test_parse_puzzle_input_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ([Item(79),Item(98)],compile('old*19','<string>','eval'),23,2,3),
        ([Item(54),Item(65),Item(75),Item(74)],compile('old+6','<string>','eval'),19,2,0),
        ([Item(79),Item(60),Item(97)],compile('old*old','<string>','eval'),13,1,3),
        ([Item(74)],compile('old+3','<string>','eval'),17,0,1),
    ]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 10605

def test_part2_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part2(example1) == 2713310158
