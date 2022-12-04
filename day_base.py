import os.path
import time
import requests
from os.path import dirname
from dotenv import load_dotenv

"""
The Day class provides a framework for all the days that are created during the Advent of Code programming calendar.
This class provides the abstraction needed in order to make sure that only the actual algorithms need to be written
for each day and not the management around it.

Original Author: Tom Meulenkamp (https://github.com/supertom01)
Date: 28-11-2022
"""


# TODO: Fix documentation to uphold Google standard
# TODO: Implement unit testing e.g. support multiple test cases
# TODO: Redo fancy formatting of logging and errors
class Day:
    def __init__(self, year: int, day_nr: int, description: str, debug=False, expected_a=None, expected_b=None):
        """
        Creates a new day object.
        It provides abstractions like a run method in order to minimize the code that has to be written for each day.
        """
        self.year = year
        self.day_nr = day_nr
        self.description = description
        self.expected_a = expected_a
        self.expected_b = expected_b
        self.debug = debug

    def __str__(self) -> str:
        return f"--- Day {self.day_nr}: {self.description} ---"

    def _get_test(self):
        """
        Grabs the test input from a text file.
        """
        try:
            with open(f'{dirname(__file__)}/test/{self.year}/day_{self.day_nr:02d}.txt', 'r') as test_file:
                return test_file.read()
        except FileNotFoundError:
            raise FileNotFoundError("No test file seems to be provided")

    def _get_input(self):
        """
        Grabs the input to be used. If the input can not be found in the cache, pull it from the AoC website
        """
        # Depending on whether we are debugging, load the example or our actual puzzle input
        input_path = f'{dirname(__file__)}/input/{self.year}/day_{self.day_nr:02d}.txt'

        # Create directories if they don't exist yet
        os.makedirs(f'{dirname(__file__)}/input/{self.year}', exist_ok=True)

        if os.path.exists(input_path):
            with open(input_path, 'r') as input_file:
                return input_file.read()

        # Load our cookie
        load_dotenv()
        session_key = os.environ["AOC_SESSION"]

        # Make a request to the AoC website for our puzzle input
        url = f"https://adventofcode.com/{self.year}/day/{self.day_nr}/input"
        request = requests.get(url, cookies={'session': session_key})

        # Cache the input for later use
        lines = request.text.strip()
        with open(input_path, 'x') as input_file:
            input_file.write(lines)
        return lines

    def _test(self, answer_a, answer_b) -> None:
        """
        Compares the actual answers with expected answers as provided in the constructor
        """
        if self.expected_a is not None and answer_a is not None:
            assert self.expected_a == answer_a, f"Part A: Expected {self.expected_a} but got {answer_a}"
        if self.expected_b is not None and answer_b is not None:
            assert self.expected_b == answer_b, f"Part B: Expected {self.expected_b} but got {answer_b}"
        # TODO: Don't say tests have passed when they actually have not
        print("Test(s) passed")

    def part_a(self, parsed_puzzle_input) -> int:
        """
        Calculates the solution for the first part of the days puzzle
        """
        raise NotImplementedError("Part A has not yet been implemented")

    def part_b(self, parsed_puzzle_input) -> int:
        """
        Calculates the solution for the second part of the days puzzle
        """
        raise NotImplementedError("Part B has not yet been implemented")

    def parse(self, puzzle_input):
        """
        Reduce the raw puzzle input to something sensible to be used by both parts
        """
        raise NotImplementedError("Parsing has not yet been implemented")

    def run(self):
        """
        Executes each part of the day and measures the time it takes to execute it.
        """
        print(self)

        # Based on the debug flag we take the provided example or actual input
        if self.debug:
            puzzle_input = self._get_test()
        else:
            puzzle_input = self._get_input()

        parsed_puzzle_input = self.parse(puzzle_input)

        answer_a = None
        answer_b = None
        try:
            before = time.time()
            answer_a = self.part_a(parsed_puzzle_input)
            after = time.time()
            print(f'Part A: {answer_a} (computation time: {(after - before) * 1000:.5f} ms)')
        except NotImplementedError as error:
            print(error)
        try:
            before = time.time()
            answer_b = self.part_b(parsed_puzzle_input)
            after = time.time()
            print(f'Part B: {answer_b} (computation time: {(after - before) * 1000:.5f} ms)')
        except NotImplementedError as error:
            print(error)

        # If we're in debug mode, check if the answers are as expected
        if self.debug:
            self._test(answer_a, answer_b)
