import pathlib
import pytest
import aoc201507 as aoc

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
        ("x AND y", "d"),
        ("x OR y", "e"),
        ("x LSHIFT 2", "f"),
        ("y RSHIFT 2", "g"),
        ("NOT x", "h"),
        ("NOT y", "i"),
        ("123", "x"),
        ("456", "y")
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456
    }


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...