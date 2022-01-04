
class Node:
    def __init__(self, name):
        self.name = name        # For example: 'start', 'A', or 'xy'
        self.neighbours = set() # Set of neighbouring nodes


if __name__ == '__main__':
    # Perform setup
    caves = set()
    # Parse input
    with open('input/Day') as f:
        for edge in f.read().split('\n'):