# My Advent of Code solutions
I like to brush up my coding skills with [Advent of Code](https://adventofcode.com/) puzzles.

## HOWTO run individual solutions
I make use of the [Advent of Code Data library](https://pypi.org/project/advent-of-code-data/), which can cache puzzle data.

## HOWTO Solve for a new day
Inspired by the [Real Python article](https://realpython.com/python-advent-of-code/), I started to use templates 
and perform automated testing on provided examples before running my code on the actual input.

To automatically create and populate the provided templates, run the `copier copy copier_template .` command. This will 
ask you for what year and day you want to generate the solution and test files. Makes use of [copier](https://copier.readthedocs.io/en/stable/)

Example code is expected to be found in files `example1.txt` and up. Implement your solutions in the appropriate functions 
and enable the relevant tests.

## TODO
- [ ] Make copier instantiate years and days as packages
  - [ ] Reconsider having folders for years start with number. This makes imports impossible.
- [ ] For copier, make current date the default
- [ ] Rewrite template to be class based (Use [Tom Meulenkamp](https://github.com/supertom01/adventOfCode) as example)
  - [ ] Make class diagram design
  - [ ] Include timing of execution
  - [ ] Rewrite existing code to be used with classes
- [ ] Rewrite existing solutions using regex & groups
