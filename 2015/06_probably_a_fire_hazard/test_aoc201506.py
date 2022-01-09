import pathlib
import pytest
import aoc201506 as aoc

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
    """Test that input is parsed properly"""
    assert example1 == [
        ("turn on", 0, 0, 999, 999),
        ("toggle", 0, 0, 999, 0),
        ("turn off", 499, 499, 500, 500)
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 1e6 - 1000 - 4  # all on, toggle first row off and turn middle 4 off


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 2000000 + 1 - 1
